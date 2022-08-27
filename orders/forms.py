from django import forms
from .models import Order
from localflavor.us.forms import USZipCodeField



class OrderCreatForm(forms.ModelForm):
    postal_code = USZipCodeField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'postal_code']