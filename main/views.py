from django.shortcuts import render, redirect
from .models import Products, Home_content, Home_Slider
from .forms import SubForm, ProductsForm
from django.views.generic import DeleteView, UpdateView, DetailView

class PostUpdateView(UpdateView):
    model = Products
    template_name = 'main/create_card.html' 
    form_class = ProductsForm

class PostDeleteView(DeleteView):
    model = Products
    template_name = 'main/card-delete.html' 
    success_url = '/'

def index(request):
    us = request.user
    array = ['1', '2', '3', '4', '5', '6', '7', '8']
    product = Products.objects.all()
    home = Home_content.objects.all()
    slider = Home_Slider.objects.all()
    post_count = Products.objects.count()
   
    error = ''
    if request.method == "POST":
        form = SubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заполнена некоректно'

    form = SubForm()
    context = {
            "product": product, 
            "home": home,
            "slider": slider,
            "array": array,
            'form': form,
            'error': error,
            'us' : us,
            'post_count' : post_count
            }
   
    return render(request, 'main/index.html', context)
    
def cart(request):
    return render(request, 'main/cart.html')

def categories(request):
    product = Products.objects.all()
    post_count = Products.objects.count()
    us = request.user
    context = {
        "product": product, 
        'post_count' : post_count,
        'us' : us
        }
    return render(request, 'main/cards_list.html', context)

def checkout(request):
    return render(request, 'main/checkout.html')

def auth(request):
    return render(request, 'main/auth.html')

def registration(request):
    return render(request, 'main/registration.html')

def create_card(request):
    error = ''
    if request.method == "POST":
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заполнена некоректно'

    form = ProductsForm()

    data = {
        'form': form,
        'error': error,
    }

    return render(request, 'main/create_card.html', data)


class XarakteristikiDetailView(DetailView):
    model = Products
    template_name = 'main/xarakteristiki.html'
    context_object_name = 'xar'