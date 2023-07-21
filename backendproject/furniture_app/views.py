from urllib import request

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer, Category, Product
from .serializers import CustomerSerializer, CategorySerializer, ProductSerializer

"""
CustomerView: To manage customer information
:param request: url body
:param args and kwargs: system variables to pass along url
:return : HTTP response
"""


# Create your views here.
class CustomerView(APIView):
    def post(self, request):

        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if Customer.objects.filter(user_name=serializer.validated_data.get('user_name')).exists():
                return Response({'status': 'error - user already exists'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, status=status.HTTP_400_BAD_REQUEST)


"""
Class CategoryView: To manage product category information
:param request: url body
:return : HTTP response

"""


class CategoryView(APIView):

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, status=status.HTTP_400_BAD_REQUEST)

class CategoriesView(APIView):

    def get(self, request):
        results = Category.objects.all()
        serializer = CategorySerializer(results, many=True)
        return Response({'status': 'success', 'customers': serializer.data})

class ProductByCategoryView(APIView):
    def get(self, request,*args,**kwargs):
        category = kwargs.get('category')
        results = Product.objects.filter(category=category)
        serializer = ProductSerializer(results, many=True)
        return Response({'category':category,'product': serializer.data},status=status.HTTP_200_OK)

class ProductView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):

    def post(self, request):
        user_name = request.data["user_name"]
        password = request.data["password"]
        try:
            user = Customer.objects.get(user_name=user_name)
        except Customer.DoesNotExist:
            user = None
        if user is not None:
            serializer = CustomerSerializer(user)
            if password != serializer.data['password']:
                return Response({"response": "Incorrect password"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"response": "login successful"}, status=status.HTTP_200_OK)
        else:
            return Response({"response": "user does not exist"}, status=status.HTTP_400_BAD_REQUEST)
