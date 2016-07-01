from django.contrib import admin
from .models import Producto, Favorite

# Register your models here.
#admin.site.register(Producto)
@admin.register(Producto)
class AdminProducto(admin.ModelAdmin):
    list_display = ('name', 'category', 'descripcion',)
    list_filter = ('category',)

@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
    list_display = ('user', 'product',)
    list_filter = ('user', 'product',)