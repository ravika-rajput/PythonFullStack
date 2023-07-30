from .views import CustomerView, CategoryView, ProductView, LoginView, CategoriesView, ProductByCategoryView, \
    InvoiceView, InvoiceViewUsername
from django.urls import path

urlpatterns = [

    path('register/', CustomerView.as_view()), #customer registration
    path('category/', CategoryView.as_view()), #category creation
    path('categories/', CategoriesView.as_view()), #to get list of categories
    path('product/', ProductView().as_view()), #to register a new product
    path('product/<str:category>', ProductByCategoryView().as_view()), #to filter product based on a category
    path('login/', LoginView().as_view()), #customer login
    path('invoice/', InvoiceView().as_view()), #invoice creation
    path('invoice/<str:user_name>', InvoiceViewUsername().as_view()) #get invoice by user name
]
