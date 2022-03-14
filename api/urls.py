from unicodedata import name
from django.urls import path
from api import views



urlpatterns = [
    path('',views.ApiView.as_view(),name="product"),
    path('product/', views.ProductView.as_view(), name='add-product'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
]