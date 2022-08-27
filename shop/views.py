from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm
from .recommender import Recommender



# def home(request):
#     return render(request, 'shop/home.html', {})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        # for adapting the view in translation mode
        language = request.LANGUAGE_CODE
        category = get_object_or_404(Category, translations__language_code=language, 
                                    translations__slug=category_slug)
        products = products.filter(category=category)
    
    return render(request, 'shop/home.html', {'category':category, 'categories':categories, 'products':products})


def product_detail(request, id, slug):
    language = request.LANGUAGE_CODE
    product = get_object_or_404(Product, id=id, translations__language_code=language, 
                                translations__slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    r= Recommender()
    recommended_products = r.suggest_products_for([product], 3)
    return render(request, 'shop/product_detail.html', {'product':product, 'cart_product_form':cart_product_form,
                                                        'recommended_products':recommended_products})