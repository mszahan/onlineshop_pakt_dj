from django import forms
from django.db.models import fields
from .models import Order



class OrderCreatForm(forms.ModelForm):
    model = Order
    fields = ['first_name', 'last_name', 'email', 'address', 'city', 'postal_code']