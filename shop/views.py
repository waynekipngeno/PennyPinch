from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .models import Product
from .forms import ProductForm

# Create your views here.
@login_required
def newpurchase(request):
    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)

        if product_form.is_valid():
            cd = product_form.cleaned_data
            new_item = product_form.save(commit=False)
            new_item.buyer = request.user
            new_item.save()
            product_form.save()
            messages.success(request, 'Your order has been posted successfully!')
            return redirect(new_item.get_absolute_url())
    else:
        product_form = ProductForm()
    return render(request, 'product/newpurchase.html', {'product_form':product_form,})

def purchase_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'product/purchase_detail.html', {'product':product,})
