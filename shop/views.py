from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Product, Contact
from math import ceil
# Create your views here.


def home(request):
    products = Product.objects.all()
    allprods = []
    catprod = Product.objects.values('category')
    params = {'catprod': catprod, 'products': products}
    return render(request, 'home.html', params)


def detail(request, myid):
    prod = Product.objects.filter(id=myid)
    return render(request, 'detail.html', {'product': prod[0]})


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        query = request.POST.get('query', '')
        # print(name,email,phone,query)
        contact = Contact(name=name, email=email, phone=phone, query=query)
        contact.save()
        return redirect('home')
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')
def category(request):
    return render(request,'category.html')