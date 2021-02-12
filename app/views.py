from django.shortcuts import render
from app.models import Computer, VideoCard, Motherboard, Ram, HardDrive, Processor
from django.http import HttpResponse
import app.templates
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.views.generic import DeleteView
from django.utils.translation import ugettext as _

def pc_sets(request):
    context = {"Parts": ["Video cards", "Ram's", "Processors", "Main memory", "Motherboards"],
               "header": "Show all parts", }
    return render(request, "index.html", context)


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
    return render(request,"videocards.html", {})

def to_motherboards(request):
    return render(request, "motherboards.html", {})


class ProductDetailViev(DeleteView):

    CT_MODEL_MODEL_CLASS = {
        "computer": Computer,
        "videocard" : VideoCard,
        "ram" : Ram,
        "harddrive" : HardDrive,
        "motherboard" : Motherboard,
        "processor" : Processor
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs["ct_model"]]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)


    context_object_name = "product"
    template_name = "product_detail.html"
    slug_url_kwarg = "slug"





