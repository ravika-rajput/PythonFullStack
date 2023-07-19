from django.contrib import admin
from .models import Customer, Category, Product, Login

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Login)
