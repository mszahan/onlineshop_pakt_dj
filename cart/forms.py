from django import forms
from django.utils.translation import gettext_lazy as _


PRODUCT_QUANTITY_CHOICHES = [(i, str(i)) for i in range(1, 6)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICHES, coerce=int, label=_('Quantity'))
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    