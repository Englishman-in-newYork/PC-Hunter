from django.urls import include, path


from app.views import *

urlpatterns = [
    path("Main/", BaseViev.as_view(), name = "Main"),
    path("loggin-check", do_login),
    path("login-page", go_to_loggin, name = "login-page"),
    path("back", to_main),
    path("logout", do_logout, name = "logout"),
    path("go_to_regist", regist_page, name ="registration"),
    path("registration", register),
    path("ajax_test", ajax_test),
    path("check_login",validation),
    path("go_to_components", to_components, name = "components"),
    path("go_to_videocards", to_videocards),
    path("go_to_motherboards", to_motherboards),
    path("products/<str:ct_model>/<str:slug>/", ProductDetailViev.as_view(), name = "product_detail"),
    path("category/<str:slug>/", CategoryDetailViev.as_view(), name = "category_detail"),
    path("cart/", CartViev.as_view(), name = "cart"),
    path("add_to_cart/<str:ct_model>/<str:slug>/", AddToCartViev.as_view(), name = "add_to_cart"),
    path("remove_from_cart/<str:ct_model>/<str:slug>/", DeleteFromCartViev.as_view(), name = "delete_from_cart"),
    path("change-qty/<str:ct_model>/<str:slug>/", ChangeQTYViev.as_view(), name = "change_qty"),
    path("checkout/", CheckoutViev.as_view(), name = "checkout"),
    path("makeorder/", MakeOrderViev.as_view(), name = "make_order")

    #path("get_csv", get_csv)
    #path("person", server),
]
