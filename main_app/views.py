from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import User, Property, Image
from django.core.files.storage import FileSystemStorage
import os
# from django.contrib.staticfiles.utils import get_files
# from django.contrib.staticfiles.storage import StaticFilesStorage

# Create your views here.

def home(request):
    return render(request, template_name="main_app/index.html")

def platform_info(request):
    return render(request, template_name="main_app/platformInfo.html")

def covid_info(request):
    return render(request, template_name="main_app/covidInfo.html")

def login_page(request):
    context = {
        'login': True,
    }
    return render(request, template_name="main_app/login.html", context=context)

def signup_page(request):
    context = {
        'login': False,
    }
    return render(request, template_name="main_app/login.html", context=context)

def create_account(request):

    email = request.POST.get('unregisteredEmail')
    name = request.POST.get('name')
    password = request.POST.get('password')
    category = request.POST.get('category')

    if User.objects.filter(email=email).first() is None:
        # works
        user = User.objects.create(name=name, email=email, password=password, category=category)
        context = {
            'login': True,
            'message': 'Account created successfully. Now login.',
        }
        return render(request, template_name='main_app/login.html', context=context)
    else:
        # user exists
        context = {
            'login': False,
            'message': 'Account already exists',
        }
        return render(request, template_name='main_app/login.html', context=context)

    # return render(request, template_name="main_app/dashboard.html")


def login(request):

    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.filter(email=email, password=password).first()
    if user is None:
        context = {
            'login': True,
            'message': 'Username or Password are wrong.',
        }
        return render(request, template_name='main_app/login.html', context=context)

    request.session['email'] = email
    properties = []
    if user.category != 'warrior':
        props = Property.objects.filter(owner=email).all()

    return render(request, template_name='main_app/dashboard.html', context={'category': user.category, 'properties': props,})


def search_result(request):
    search = request.POST.get('search')
    # print(search)
    context = {
        'search': search,
    }
    return render(request, 'main_app/searchResults.html', context=context)


def add_property(request):

    return render(request, template_name='main_app/addProperty.html')

def save_property(request):
    owner = request.session['email']
    street = request.POST.get('street')
    city = request.POST.get('city')
    state = request.POST.get('state')
    pincode = request.POST.get('pincode')
    country = request.POST.get('country')

    photo = request.FILES.get('image')
    # print(photo)
    loc = "media/{}/".format(request.session['email'])
    fs = FileSystemStorage(location=loc)
    if photo is not None:
        filename = fs.save(photo.name, photo)
        uploaded_file_url = fs.url(filename)
        # print(uploaded_file_url,"\n\n\n")

    # movein = request.POST.get('movein')
    # moveout = request.POST.get('moveout')
    rent = request.POST.get('rent')
    notes = request.POST.get('notes')
    if rent == '' or rent is None:
        rent = 0.0
    else:
        rent = float(rent)

    prop = Property.objects.create(owner=owner,number_and_street=street, pincode=pincode, city=city, state=state, country=country, rent=rent, notes=notes)
    img = Image.objects.create(post=prop, photo=photo)

    path = "{}/media/{}/".format(os.getcwd(), request.session['email'])
    img_list =os.listdir(path)

    # TODO: Change this
    return render(request, 'main_app/singleProperty.html', context={"image_names": img_list, "email": request.session['email'],})

def single_property(request, pk):

    path = "{}/media/{}/".format(os.getcwd(), request.session['email'])
    img_list =os.listdir(path)
    
    prop = Property.objects.get(pk=pk)
    # print(prop)
    
    return render(request, 'main_app/singleProperty.html', context={"image_names": img_list, "email": request.session['email'], "property": prop,})



# def logout(request):
#     pass