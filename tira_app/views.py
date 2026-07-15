from django.shortcuts import get_object_or_404,render, redirect
from django.shortcuts import render
from .models import Category, Product, Brand, order
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')
        
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save()
        messages.success(request,'Account created successfully! Please log in.')
        return redirect(login_user)
    
    return render(request,'register.html') 

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(username)
        print(password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # ✅ this now calls Django’s login
            return redirect('index')  # or use a proper view name
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login_user')

    return render(request, "login.html") 


def logout_user(request):
    logout(request)
    return redirect(index)

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()[:8]
    brand = Brand.objects.all()
    return render(request, 'index.html', {'categories': categories, 'products': products, "brands": brand})

def category(request, name):
    categories = Category.objects.all()
    category = Category.objects.get(name=name)
    # print(category)
    products = category.product_set.all()
    # print(products)
    brand = Brand.objects.all()
    return render(request, 'category.html', {'categories': categories,'products': products, 'brands': brand,'name': name})


def singal_product(request, product_id):
    categories = Category.objects.all()
    product = Product.objects.get(id=product_id)
    # releted product
    related_product = Product.objects.filter(category=product.category)[:8]
    brand = Brand.objects.all()
    return render(request, 'single_product.html', {'categories': categories, 'brands': brand, 'products': product, 'related_products': related_product})
