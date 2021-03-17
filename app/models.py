from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse
from django.utils import timezone

User = get_user_model()


def get_models_for_count(*model_names):
    return [models.Count(model_name) for model_name in model_names]


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={"ct_model": ct_model, "slug": obj.slug})


class LatestProductsManager:

    @staticmethod
    def get_products_for_mainpage(*args, **kwargs):
        with_respect_to = kwargs.get("with_respect_to ")
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by("-id")[:5]
            products.extend(model_products)
        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to)
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )

        return products


class LatestProducts:
    objects = LatestProductsManager()


class CategoryManager(models.Manager):
    CATEGORY_NAME_COUNT_NAME = {
        "Computers": "computer__count",
        "Video cards": "videocard__count",
        "Motherboards": "motherboard__count",
        "Processors": "processor__count",
        "RAM": "ram__count",
        "Hard drives": "harddrive__count"
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_categories_for_left_sidebar(self):
        models = get_models_for_count("computer", "videocard", "motherboard", "ram", "processor", "harddrive")
        qs = list(self.get_queryset().annotate(*models))
        data = [
            dict(name=c.name, url=c.get_absolute_url(), count=getattr(c, self.CATEGORY_NAME_COUNT_NAME[c.name]))
            for c in qs
        ]
        return data


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя категории")
    slug = models.SlugField(unique=True)
    objects = CategoryManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"slug": self.slug})


class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, verbose_name="Наименование", null=True)
    slug = models.SlugField(null=True)
    image = models.ImageField(verbose_name="Изобржение", null=True)
    description = models.TextField(verbose_name="Описание", null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Цена", null=True)

    def __str__(self):
        return self.title

    def get_model_name(self):
        return self.__class__.__name__.lower()


class CartProduct(models.Model):
    user = models.ForeignKey("Customer", verbose_name="Покупатель", on_delete=models.CASCADE)
    cart = models.ForeignKey("Cart", verbose_name="Корзина", on_delete=models.CASCADE, related_name="related_products")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Общая цена")

    def __str__(self):
        return "Продукт:{} (для корзины)".format(self.content_object.title)

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.content_object.price
        super().save(*args, **kwargs)







class Cart(models.Model):

    owner = models.ForeignKey("Customer", null=True, verbose_name="Владелец", on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name="related_cart")
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name="Общая цена")
    in_order = models.BooleanField(default=False)
    for_anonynous_user = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)



class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name="Номер телефона", null = True, blank=True)
    adress = models.CharField(max_length=255, verbose_name="Адрес", null = True, blank = True)
    orders = models.ManyToManyField("Order", verbose_name="Customer orders", related_name="related_customer")

    def __str__(self):
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Computer(Product):
    processor = models.CharField(max_length=255, verbose_name="Процессор")
    number_of_cores = models.CharField(max_length=20, verbose_name="Количество ядер")
    video_card = models.CharField(max_length=255, verbose_name="Видео карта")
    video_memory = models.CharField(max_length=20, verbose_name="Видео память")
    ram = models.CharField(max_length=20, verbose_name="Оперативная память")
    disc_type = models.CharField(max_length=20, verbose_name="Тип жесткого диска")
    disc_memory = models.CharField(max_length=20, verbose_name="Общая емкость диска")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, "product_detail")


class VideoCard(Product):
    gpu_manufacturer = models.CharField(max_length=255, verbose_name="Производитель графического процессора")
    graphics_processor = models.CharField(max_length=255, verbose_name="Графический процессор")
    gpu_frequency = models.CharField(max_length=255, verbose_name="Частота графического процессора")
    video_memory = models.CharField(max_length=255, verbose_name="Видеопамять")
    supply_power = models.CharField(max_length=255, verbose_name="Мощность блока питания")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, "product_detail")


class Motherboard(Product):
    form_factor = models.CharField(max_length=255, verbose_name="Форм фактор")
    socket = models.CharField(max_length=255, verbose_name="Сокет")
    chipset = models.CharField(max_length=255, verbose_name="Чипсет")
    memory_type = models.CharField(max_length=255, verbose_name="Тип памяти")
    memory_slots = models.CharField(max_length=255, verbose_name="Количество слотов памяти")
    processor_support = models.CharField(max_length=255, verbose_name="Поддержка процессоров")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, "product_detail")

    #     def __str__(self):
    #         if self.category is None:
    #             cat_name = ""
    #         else:
    #             cat_name = self.category.name
    #         return str(self.id)
    #
    #     def get_absolute_url(self):
    #         return get_product_url(self, "product_detail")


class Ram(Product):
    total_memory = models.CharField(max_length=255, verbose_name="Объем памяти")
    memory_type = models.CharField(max_length=255, verbose_name="Тип памяти")
    form_factor = models.CharField(max_length=255, verbose_name="Форм фактор")
    appointment = models.CharField(max_length=255, verbose_name="Назначение")
    clock_frequency = models.CharField(max_length=255, verbose_name="Тактовая частота")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, "product_detail")


class HardDrive(Product):
    model_type = models.CharField(max_length=255, verbose_name="Тип")
    form_factor = models.CharField(max_length=255, verbose_name="Форм фактор")
    data_interface = models.CharField(max_length=255, verbose_name="Интерфейс передачи данных")
    read_speed = models.CharField(max_length=255, verbose_name="Скорость чтений")
    write_speed = models.CharField(max_length=255, verbose_name="Скорость записи")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, "product_detail")


class Processor(Product):
    socket = models.CharField(max_length=255, verbose_name="Сокет")
    core_number = models.CharField(max_length=255, verbose_name="Количество ядер")
    clock_frequency = models.CharField(max_length=255, verbose_name="Тактовая частота")
    cache = models.CharField(max_length=255, verbose_name="Кэш L3")
    transistor_thickness = models.CharField(max_length=255, verbose_name="Толщина транзистора")
    memory_support = models.CharField(max_length=255, verbose_name="Поддержка памяти")

    def __str__(self):
        return "{} : {}".format(self.category.name, self.title)

    def get_absolute_url(self):
        return get_product_url(self, "product_detail")

class Order(models.Model):


    STATUS_NEW = "new"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_READY = "is_ready"
    STATUS_COMPLETED = "completed"

    BUYING_TYPE_SELF = "self"
    BUYING_TYPE_DELIVERY = "delivery"


    STATUS_CHOICES = (
        (STATUS_NEW, "New order"),
        (STATUS_IN_PROGRESS, "Order in progress"),
        (STATUS_READY, "Order ready"),
        (STATUS_COMPLETED, "Order completed")
    )

    BUYING_TYPE_CHOICES = (
        (BUYING_TYPE_SELF, "Pickup"),
        (BUYING_TYPE_DELIVERY, "Delivery")
    
    )

    customer = models.ForeignKey(Customer, verbose_name="Customer", related_name="related_orders", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, verbose_name="First name")
    last_name = models.CharField(max_length=100, verbose_name="Last name")
    phone = models.CharField(max_length= 20, verbose_name="Phone")
    cart = models.ForeignKey(Cart, verbose_name="Cart", on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=1024, verbose_name="Adress", null=True, blank=True)
    status = models.CharField(max_length=100, verbose_name="Order status", choices=STATUS_CHOICES, default=STATUS_NEW)
    buying_type = models.CharField(max_length=100, verbose_name="Order type", choices=BUYING_TYPE_CHOICES, default=BUYING_TYPE_SELF)
    comment = models.TextField(verbose_name="Comment to order", null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name="Order creation date")
    order_date = models.DateField(verbose_name="Order date", default=timezone.now)

    def __str__(self):
        return str(self.id)




class Person(models.Model):
    name = models.CharField(
        max_length=20, default=1
    )
    age = models.PositiveIntegerField(default=0)
