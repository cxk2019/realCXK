from django.shortcuts import render


def cart(request):
    return render(request,'cart.html')

def category(request):
    return render(request,'category.html')

def delete(request):
    return render(request,'delete.html')

def grounding(request):
    return render(request,'grounding.html')

def index(request):
    u=0
    if 'user' in request.COOKIES:
        u=request.COOKIES['user']
    return render(request,'index.html',{"myalert":0})

def order_history(request):
    return render(request,'order-history.html')

def order_information(request):
    return render(request,'order-information.html')

def quickview(request):
    return render(request,'quickview.html')

def register(request):
    return render(request,'register.html',{"myalert":0})

def login(request):
    return render(request,'login.html')

def product(request):
    return render(request,"product.html")