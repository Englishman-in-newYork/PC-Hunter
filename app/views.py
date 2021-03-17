from django.shortcuts import render
from django.db import transaction
from app.models import Computer, VideoCard, Motherboard, Ram, HardDrive, Processor, CategoryManager, Category, \
    Customer, Cart, CartProduct, Product
from django.http import HttpResponse
import app.templates
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.views.generic import DeleteView, View
from .mixins import CategoryDetailMixin, CartMixin
from django.contrib import messages
from .forms import OrderForm
from .utils import recalc_cart
from django.utils.translation import ugettext as _
import requests


class BaseViev(CartMixin, View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        computers = Computer.objects.all()
        context = {
            "categories": categories,
            "computers": computers,
            "cart": self.cart
        }
        return render(request, "index.html", context)


# def pc_sets(request):
#    categories = Category.objects.get_categories_for_left_sidebar()
#    return render(request, "index.html", {"categories":categories})


def go_to_loggin(request):
    return render(request, "Loggin.html", {})


def to_components(request):
    return render(request, "components.html", {})


def do_login(request):
    user = authenticate(
        username=request.POST["username"],
        password=request.POST["password"]
    )
    if user is None:
        return render(request, "error.html", {})
    else:
        login(request, user)
        return HttpResponseRedirect("Main")


def to_main(request):
    return HttpResponseRedirect("Main")


def do_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect("Main")


def regist_page(request):
    return render(request, "register.html", {})


def register(request):
    user = User.objects.create_user(
        request.POST["username"],
        password=request.POST["password"],
        email="email"
    )
    return HttpResponseRedirect("Main")


def ajax_test(request):
    response = {"message": request.POST["from_ajax"] + "blablablabal"}
    return JsonResponse(response)


def validation(request):
    users = User.objects.filter(username=request.POST["username"])
    if len(users) != 0:
        response = {"exist": 1}
    else:
        response = {"exist": 0}
    return JsonResponse(response)


def to_videocards(request):
    return render(request, "videocards.html", {})


def to_motherboards(request):
    return render(request, "motherboards.html", {})


class ProductDetailViev(CartMixin, CategoryDetailMixin, DeleteView):
    CT_MODEL_MODEL_CLASS = {
        "computer": Computer,
        "videocard": VideoCard,
        "ram": Ram,
        "harddrive": HardDrive,
        "motherboard": Motherboard,
        "processor": Processor
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs["ct_model"]]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    context_object_name = "product"
    template_name = "product_detail.html"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ct_model"] = self.model._meta.model_name
        context["cart"] = self.cart
        return context


class CategoryDetailViev(CartMixin, CategoryDetailMixin, DeleteView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = "category"
    template_name = "category_detail.html"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = self.cart
        return context


class AddToCartViev(CartMixin, View):

    def get(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get("ct_model"), kwargs.get("slug")
        customer = Customer.objects.get(user=request.user)
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            user=self.cart.owner, cart=self.cart, content_type=content_type, object_id=product.id,
        )
        if created:
            self.cart.products.add(cart_product)
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Product added")
        return HttpResponseRedirect("/cart")


class DeleteFromCartViev(CartMixin, View):

    def get(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get("ct_model"), kwargs.get("slug")
        customer = Customer.objects.get(user=request.user)
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        cart_product = CartProduct.objects.get(
            user=self.cart.owner, cart=self.cart, content_type=content_type, object_id=product.id,
        )
        self.cart.products.remove(cart_product)
        cart_product.delete()
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Product deleted")
        return HttpResponseRedirect("/cart")


class ChangeQTYViev(CartMixin, View):

    def post(self, request, *args, **kwargs):
        ct_model, product_slug = kwargs.get("ct_model"), kwargs.get("slug")
        customer = Customer.objects.get(user=request.user)
        content_type = ContentType.objects.get(model=ct_model)
        product = content_type.model_class().objects.get(slug=product_slug)
        cart_product = CartProduct.objects.get(
            user=self.cart.owner, cart=self.cart, content_type=content_type, object_id=product.id,
        )
        qty = int(request.POST.get("qty"))
        cart_product.qty = qty
        cart_product.save()
        recalc_cart(self.cart)
        messages.add_message(request, messages.INFO, "Product number changed")
        return HttpResponseRedirect("/cart/")


class CartViev(CartMixin, View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        context = {
            "cart": self.cart,
            "categories": categories
        }
        return render(request, "cart.html", context)


class CheckoutViev(CartMixin, View):

    def get(self, request, *args, **kwargs):
        categories = Category.objects.get_categories_for_left_sidebar()
        form = OrderForm(request.POST or None)
        context = {
            "cart": self.cart,
            "categories": categories,
            "form": form
        }
        return render(request, "checkout.html", context)


class MakeOrderViev(CartMixin, View):

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        customer = Customer.objects.get(user=request.user)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = customer
            new_order.first_name = form.cleaned_data["first_name"]
            new_order.last_name = form.cleaned_data["last_name"]
            new_order.phone = form.cleaned_data["phone"]
            new_order.addres = form.cleaned_data["address"]
            new_order.buying_type = form.cleaned_data["buying_type"]
            new_order.order_date = form.cleaned_data["order_date"]
            new_order.comment = form.cleaned_data["comment"]
            new_order.save()
            self.cart.in_order = True
            self.cart.save()
            new_order.cart = self.cart
            new_order.save()
            customer.orders.add(new_order)
            messages.add_message(request, messages.INFO, "Thanks for the order, the manager will contact you soon")
            return HttpResponseRedirect("/Main")
        return HttpResponseRedirect("/checkout/")

# def server(request):

#    Person.objects.filter(
#        id=request.POST["id"]
#    ).update(
#        name = request.POST["name"],
#        age = int(request.POST["age"])
#    )
#    if len(request.POST["age"]) > 3 or len(request.POST["name"]) > 20:
#        return ValueError
#    else:
#        JsonResponse({"status": "ok"})

# import csv

# def get_csv(request):
#    responce = HttpResponse(content_type="text/csv")
#    responce["Content-Disposition"] = 'attachment; filename"somefilename.csv" '

#    stuff = csv.writer(responce)
#    stuff.writerow(["id", "video_memory"])
#    cards = VideoCard.objects.all()
#    for card in cards:
#        stuff.writerow([card.id, card.video_memory])
#    return responce
