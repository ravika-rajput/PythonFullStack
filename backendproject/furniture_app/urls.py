from .views import CustomerView, CategoryView, ProductView, LoginView, CategoriesView, ProductByCategoryView, \
    InvoiceView, InvoiceViewUsername
from django.urls import path

urlpatterns = [

    path('register/', CustomerView.as_view()),
    path('category/', CategoryView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('product/', ProductView().as_view()),
    path('product/<str:category>', ProductByCategoryView().as_view()),
    path('login/', LoginView().as_view()),
    path('invoice/', InvoiceView().as_view()),
    path('invoice/<str:user_name>', InvoiceViewUsername().as_view())
]
