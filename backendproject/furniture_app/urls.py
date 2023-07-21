from .views import CustomerView, CategoryView, ProductView, LoginView, CategoriesView, ProductByCategoryView
from django.urls import path

urlpatterns = [
    #path('customers/', CustomerView.as_view()),
    path('register/', CustomerView.as_view()),
    #path('customers/<str:user_name>', CustomerView.as_view()),
    path('category/', CategoryView.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('product/', ProductView().as_view()),
    path('product/<str:category>', ProductByCategoryView().as_view()),
    path('login/', LoginView().as_view())
]
