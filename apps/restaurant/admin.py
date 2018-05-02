from django.contrib import admin
from .models import Restaurant, Category, Product, Details

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Details)
