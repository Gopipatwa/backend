from django.contrib import admin
from api.models import Product,Users

# Register your models here.

# admin.site.register(Users)
# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','add_date','quantity','image']

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'username']