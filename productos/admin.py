from django.contrib import admin
from .models import Producto
# Register your models here.
#admin.site.register(Producto)
@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
    list_display = ('name', 'category', 'descripcion',)
    list_filter = ('category',)