from django import forms

from  .models import Product
from urllib import request
from django.utils.text import slugify
from django.core.files.base import ContentFile

class ProductForm(forms.ModelForm):
    class Meta:
        model       = Product
        fields      = ['name', 'category', 'condition', 'description', 'image']

        widgets     = {
            'name':forms.TextInput(attrs={'class':'form__input',}),
            'category':forms.Select(attrs={'class':'form__input',}),
            'condition':forms.Select(attrs={'class':'form__input',}),
            'description':forms.Textarea(attrs={'class':'form__input',}),
            'image':forms.FileInput(attrs={'class':'form__input',}),

      }
    