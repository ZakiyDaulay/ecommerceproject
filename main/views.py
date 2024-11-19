from django.shortcuts import render,redirect
from main.forms import ProductEntryForm
from main.models import ProductEntry
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import  login,logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

@login_required(login_url='/login')
def show_main(request):

    context = {
        'Name_APP' : 'TOKO HITAM',
        'Name': request.user.username,
        'Class': 'KKI',
        'NPM': '2306170130',
        'last_login':request.COOKIES.get('last_login','No recent login information')

    }

    return render(request, "main.html", context)


def show_xml(request):
    data = ProductEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
def show_json(request):
    data = ProductEntry.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_product_entry(request):
    form=ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry=form.save(commit=False)
        product_entry.user=request.user
        product_entry.save()
        return redirect('main:show_main')
    context = {'form': form}
    return render(request,"create_product_entry.html",context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

       
        if form.is_valid():
            user = form.get_user()
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm(request)
        
    context = {'form': form}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('main:login')

def show_xml_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = ProductEntry.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def edit_product(request, id):

    product = ProductEntry.objects.get(pk = id)


    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":

        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
   
    product = ProductEntry.objects.get(pk = id)

    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    name = strip_tags(request.POST.get("name")) # strip HTML tags!
    description = strip_tags(request.POST.get("description")) # strip HTML tags!
    price = request.POST.get("price")
    user = request.user

    new_product = ProductEntry(
        name=name, description=description,
        price=price,
        user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':

        data = json.loads(request.body)
        new_product = ProductEntry.objects.create(
            user=request.user,
            name=data["name"],
            price=int(data["price"]),
            description=data["description"]
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)