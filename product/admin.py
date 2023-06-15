from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','market_price','category']


admin.site.register(Product,ProductAdmin)

