from django import forms

class ProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'