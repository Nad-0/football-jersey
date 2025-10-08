from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.contrib.auth.models import User


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "all":
        product_list = Product.objects.exclude(id__isnull=True)
    else:
        product_list = Product.objects.filter(user=request.user).exclude(id__isnull=True)

    context = {
        'npm': '2406348774',
        'name': 'Go Nadine Audelia',
        'kelas': 'PBP C',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)


def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        news_entry = form.save(commit = False)
        news_entry.user = request.user
        news_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
            'jersey_views': product.jersey_views,
            'is_jersey_hot': product.is_jersey_hot,
            'created_at': product.created_at.isoformat() if product.created_at else None,
        }
        for product in product_list
    ]
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_list = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_list)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user.id if product.user else None,
            'jersey_views': product.jersey_views,
            'is_jersey_hot': product.is_jersey_hot,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

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
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)
   
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login') 
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    if product.user != request.user:
        return HttpResponse("You are not authorized to access this page.", status=403)
    form = ProductForm(instance=product)

    context = {
        'form': form,
        'product': product  
    }
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@login_required
def create_product_ajax(request):
    if request.method == 'POST':
        name = strip_tags(request.POST.get('name'))
        price = request.POST.get('price')
        description = strip_tags(request.POST.get('description'))
        category = request.POST.get('category')
        thumbnail = request.POST.get('thumbnail')
        is_featured = bool(request.POST.get('is_featured'))

        new_product = Product(
            name=name,
            price=price,
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=request.user
        )
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def ajax_register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "message": "Username already exists!"})
        User.objects.create_user(username=username, password=password)
        return JsonResponse({"success": True, "message": "Your account has been successfully created!"})
    return JsonResponse({"success": False, "message": "Invalid method!"})

@csrf_exempt
def ajax_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            response = JsonResponse({"success": True})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({"success": False, "message": "Username or password is incorrect!"})

    return JsonResponse({"success": False, "message": "Invalid method!"})

@csrf_exempt
def ajax_get_product(request):
    products = Product.objects.all().order_by('-created_at') 
    
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'thumbnail': product.thumbnail,
            'category': product.get_category_display(),
            'is_featured': product.is_featured,
            'is_jersey_hot': product.is_jersey_hot, 
            'user_id': product.user.id if product.user else None,
            'created_at': product.created_at.strftime('%b %d, %Y'), 
        })
        
    return JsonResponse(data, safe=False)

@csrf_exempt
def ajax_add_product(request):
    if request.method == "POST":
        name = request.POST.get("name")
        price = request.POST.get("price")
        stock = request.POST.get("stock")

        product = Product.objects.create(name=name, price=price, stock=stock)
        return JsonResponse({"success": True, "id": product.id})
    return JsonResponse({"success": False})

@login_required 
def ajax_edit_product(request, id):
    if request.method == "POST":
        product = get_object_or_404(Product, pk=id)
        form = ProductForm(request.POST, instance=product)
        
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "message": "Product updated successfully!"})
        else:
            return JsonResponse({"success": False, "message": "Invalid data.", "errors": form.errors}, status=400)
            
    return JsonResponse({"success": False, "message": "Invalid request method."}, status=405)

@csrf_exempt
def ajax_delete_product(request, id):
    if request.method == "DELETE":
        Product.objects.filter(pk=id).delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})
    