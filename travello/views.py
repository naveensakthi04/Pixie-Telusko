from django.shortcuts import render
# Create your views here.
from travello.models import Product


def home(request):
    products = Product.objects.all()

    return render(request,
                  'index.html',
                  {'products': products},
                  )
