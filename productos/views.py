from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto
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