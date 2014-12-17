from django.contrib import admin
from product.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
	fields = ['title', 'description', 'image']

admin.site.register(Product, ProductAdmin)