from django.shortcuts import render, redirect, get_object_or_404
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    object = Phone.objects.all()
    sort = request.GET.get('sort', 1)
    if sort == 'name':
        object = Phone.objects.order_by('name')
        context = {'phones': object}
    elif sort == 'max_price':
        object = Phone.objects.order_by('-price')
        context = {'phones': object}
    elif sort == 'min_price':
        object = Phone.objects.order_by('price')
        context = {'phones': object}          
    else:
        context = {'phones': object}  
    return render(request, template, context)


def show_product(request, slug):
    post = get_object_or_404(Phone, slug=slug)
    template = 'product.html'
    context = {'phone': post}
    return render(request, template, context)





