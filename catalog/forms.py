import sys

from django import forms
from .models import Product


class CatalogProductForm(forms.ModelForm):
    """Catalog product form"""
    error_css_class = 'my-custom-error-class'

    def clean(self):
        denied_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', 'fuck']
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        desc = cleaned_data.get('desc')
        if any(word in name for word in denied_words):
            self.add_error('name', 'Obsolete lexic')
        if any(word in desc for word in denied_words):
            self.add_error('desc', 'Obsolete lexic')
        return cleaned_data

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            # Example: Check image dimensions
            try:
                if image.size > 5242880:
                    raise forms.ValidationError("Image dimensions too large. Max 5 Mb.")
            except IOError:
                raise forms.ValidationError("Invalid image file.")
        return image

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Price must be positive")
        return price

    class Meta:
        model = Product
        fields = ['category', 'name', 'desc', 'price', 'image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*'}),
        }

    def __init__(self, *args, **kwargs):
        super(CatalogProductForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs.update({'class': 'form-control'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
        self.fields['image'].required =False
        self.fields['name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Product name'})
        self.fields['desc'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Product description'})
