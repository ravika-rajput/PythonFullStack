from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Customer, Category, Product
from .serializers import CustomerSerializer, CategorySerializer, ProductSerializer


# Create your views here.
class CustomerView(APIView):
    def get(self, request, *args, **kwargs):
        user_name = kwargs.get('user_name')
        print(user_name)
        if user_name:
            results = Customer.objects.get(user_name=user_name)
            serializer = CustomerSerializer(results)
            return Response({'status': 'success', 'customers': serializer.data}, status=status.HTTP_200_OK)

        else:
            results = Customer.objects.all()
            serializer = CustomerSerializer(results, many=True)
            return Response({'status': 'success', 'customers': serializer.data})

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, status=status.HTTP_400_BAD_REQUEST)


class CategoryView(APIView):
    def get(self, request):
        results = Category.objects.all()
        serializer = CategorySerializer(results, many=True)
        return Response({'status': 'success', 'customers': serializer.data})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, status=status.HTTP_400_BAD_REQUEST)


class ProductView(APIView):

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'status': 'error', 'data': serializer.data}, status=status.HTTP_400_BAD_REQUEST)


