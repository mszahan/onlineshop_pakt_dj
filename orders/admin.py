from django.contrib import admin
from django.db import models
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product',]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                     'postal_code', 'city', 'paid', 'created', 'update'] 
    list_filter = ['paid', 'created', 'update']
    inlines = (OrderItemInline,)
