from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Producto
from forms import ProductForm
# Create your views here.

def hello_world(request):
    #return HttpResponse("Hello World!")
    #return render(request, "index.html")
    producto = Producto.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'product': producto
    }
    return HttpResponse(template.render(context, request))

def product_detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    template = loader.get_template('product_detail.html')
    context = {
        'product': producto
    }
    return HttpResponse(template.render(context, request))

def new_product(request):
    template = loader.get_template('new_product.html')
    form = ProductForm()
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))