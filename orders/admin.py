import csv
from curses.ascii import HT
import datetime
from django.http import HttpResponse
from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product',]


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    content_disposition = f'attachment; filename={opts.verbose_name}.csv'
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = content_disposition
    writer = csv.writer(response)

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    #write first row with header information
    writer.writerow([field.verbose_name for field in fields])
    #write data rows
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
    return response

export_to_csv.short_description = 'Export to CSV'



# for changing the view of the order admin pannel and using the customized template
# This is a function that takes an Order object as........ 
# an argument and returns an HTML link for the admin_order_detail URL

def order_detail(obj):
    url = reverse('admin_order_detail', args = [obj.id])
    return mark_safe(f'<a href="{url}"> View </a>')



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', order_detail, 'first_name', 'last_name', 'email', 'address',
                     'postal_code', 'city', 'paid', 'created', 'update'] 
    list_filter = ['paid', 'created', 'update']
    inlines = (OrderItemInline,)
    actions = [export_to_csv]
