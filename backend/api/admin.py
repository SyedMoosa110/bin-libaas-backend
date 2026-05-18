from django.contrib import admin
from .models import Product, Order, Message, StoreSettings

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Message)
admin.site.register(StoreSettings)
