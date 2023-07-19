from rest_framework import serializers
from .models import Customer, Category, Product


class CustomerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(max_length=200, required=True)
    last_name = serializers.CharField(max_length=200, required=True)
    user_name = serializers.CharField(max_length=200, required=True)
    email = serializers.CharField(max_length=200, required=True)
    mobile_num = serializers.CharField(max_length=10, required=True)
    address = serializers.CharField(max_length=500, required=True)
    password = serializers.CharField(max_length=20, required=True)

    class Meta:
        model = Customer
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    type = serializers.CharField(max_length=200, required=True)

    class Meta:
        model = Category
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    prod_name = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=500)
    condition = serializers.CharField(max_length=100)
    days_to_deliver = serializers.IntegerField()
    category = serializers.CharField(max_length=100)
    color = serializers.CharField(max_length=100)
    size = serializers.CharField(max_length=100)
    image_url = serializers.CharField(max_length=500)
    rate = serializers.FloatField()

    class Meta:
        model = Product
        fields = ('__all__')



