from django.shortcuts import render
# from .products import products
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product 
from .serializer import ProductSerializer
# Create your views here.

@api_view(['GET'])
def get_products(request, pk = "0" ):
    if pk != "0":
        products = Product.objects.get(_id = int(pk))
        many_val = False
    else:
        products = Product.objects.all()
        many_val = True
    product_serializer = ProductSerializer(products, many = many_val)
    return Response(product_serializer.data)


