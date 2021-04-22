from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.forms import UserCreationForm
from.forms import SignUpForm


# Create your views here.


def index(request):
    print(request.user)
    if request. user. is_anonymous:
        return redirect("/login")
  

    products = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)

    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request, 'index.html', data)

def validateCustomer(customer):
    error_message=None;
    if(not customer.first_name):
        error_message = "First Name required!!"
    elif len(customer.first_name) < 4:
        error_message = "first name should be 4 char long or more"

    elif not customer.last_name:
        error_message = "last name required"
    elif len(customer.last_name) < 4:
        error_message = "last name should be 4 char long or more "

    elif len(customer.email) < 5:
        error_message = "email should be 5char long or more "

    elif not customer.phone:
        error_message = "Phone Number required"
    elif len(customer.phone) < 10:
        error_message = "Phone number should be 10 char long or more "

    elif len(customer.password) < 6:
        error_message = "password should be 6 char long or more "
        
    elif customer.isExists():
        error_message="Email address already registered"
        
        return error_message


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def loginUser(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
    
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request,'login.html')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')