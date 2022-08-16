from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from shop.models import Product
from coupons.models import Coupon


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True, auto_now_add=False)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, related_name='orders', null=True)
    discount = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return f"Order: {self.id}"
    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal(100))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_item')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return str(self.id)
    def get_cost(self):
        return self.price * self.quantity