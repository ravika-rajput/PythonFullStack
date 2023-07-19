from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    mobile_num = models.CharField(max_length=10)
    address = models.CharField(max_length=500)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.email + " " + self.mobile_num + " " + self.address + " " + self.password


class Category(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Product(models.Model):
    prod_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    condition = models.CharField(max_length=100)
    days_to_deliver = models.IntegerField()
    category = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500)
    rate = models.FloatField()

    def __str__(self):
        return self.prod_name + " " + self.description + " " + self.condition + " " + self.days_to_deliver + " " + self.category + " " + self.color + " " + self.size + " " + self.image_url + " " + self.rate


class Login(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name + " " + self.password
