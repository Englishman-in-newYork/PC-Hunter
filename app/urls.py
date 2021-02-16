from django.urls import include, path


from app.views import to_main,to_videocards, do_logout, go_to_loggin, do_login, pc_sets, register, regist_page,\
    ajax_test, validation, to_components,to_motherboards, ProductDetailViev

urlpatterns = [
    path("Main", pc_sets, name = "Main"),
    path("loggin-check", do_login),
    path("login-page", go_to_loggin),
    path("back", to_main),
    path("logout", do_logout),
    path("go_to_regist", regist_page),
    path("registration", register),
    path("ajax_test", ajax_test),
    path("check_login",validation),
    path("go_to_components", to_components),
    path("go_to_videocards", to_videocards),
    path("go_to_motherboards", to_motherboards),
    path("products/<str:ct_model>/<str:slug>/", ProductDetailViev.as_view(), name = "product_detail"),
]
