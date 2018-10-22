from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from ..vehicles.models import Category, Vehicles
from .serializers import VehiclesSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework import viewsets

# The root of our API is going to be a view that supports listing all the existing snippets, or creating a new snippet

@csrf_exempt
def vehicles_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        vehicles = Vehicles.objects.all()
        serializer = Vehicles(vehicles, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = VehiclesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def vehicles_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        vehicles = Vehicles.objects.get(pk=pk)

    except Vehicles.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = VehiclesSerializer(vehicles)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = VehiclesSerializer(vehicles, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        vehicles.delete()
        return HttpResponse(status=204)


@csrf_exempt
def category_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':

        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def category_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        category = Category.get(pk=pk)

    except Category.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = CategorySerializer(category)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        category.delete()
        return HttpResponse(status=204)

# from django.shortcuts import render, get_object_or_404
#
# from cart.forms import CartAddProductForm
# from .models import Category, Product
#
#
# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#                   'shop/product/list.html',
#                   {'category': category,
#                    'categories': categories,
#                    'products': products})
#
#
# def product_detail(request, product_id, slug):
#     product = get_object_or_404(Product,
#                                 id=product_id,
#                                 slug=slug,
#                                 available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request,
#                   'shop/product/detail.html',
#                   {'product': product,
#                    'cart_product_form': cart_product_form})
