from django.contrib import admin
from app.models import *
from django.forms import  ModelChoiceField



class ComputerAdmin(admin.ModelAdmin):


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "category":
            return ModelChoiceField(Category.objects.filter(slug = "computers"))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



admin.site.register(VideoCard)
admin.site.register(Motherboard)
admin.site.register(Ram)
admin.site.register(Computer)
admin.site.register(HardDrive)
admin.site.register(Processor)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
admin.site.site_url ="/Main"
admin.site.register(Order)