from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreatForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreatForm(request.POST)
        if form.is_valid():
            order= form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                        product=item['product'],
                                        price=item['price'],
                                        quantity=item['quantiy'])
            #clear the cart
            cart.clear()
            return render(request, 'create_order.html', {'order':order})
        else:
            form = OrderCreatForm()
            return render(request, 'create_order.html', {'cart':cart, 'form':form} )

