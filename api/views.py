# from django.shortcuts import render
from api.serializers import UserSerializers,UserLoginSerializers,ProductSerializers
from api.models import Users,Product
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view
# # Create your views here.
from rest_framework.views import APIView
from rest_framework import status
import json
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import generics
# # from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework import viewsets



class ApiView(generics.ListAPIView):
    serializer_class = UserLoginSerializers
    queryset = Users.objects.all()
    def get(self,request):
        api_urls = {
        'List':'/product/',
        'Detail View':'/product/<str:pk>/',
        'Create':'product/add/',
        'Update':'product-update/<str:pk>/',
        'Delete':'/product-delete/<str:pk>/'}
        return Response(api_urls)

class LoginView(APIView):
    permission_classes = (AllowAny,)
    queryset = Users.objects.all()
    def post(self,request):
        username=request.data['username']
        psd=request.data['password']
        print(username,psd)
        auth = authenticate(username=username,password=psd)
        if auth:
            return Response({'message':"success","username":username,"password":psd})
        else:
            return Response({"message":"invalid authenticate"})

class RegisterView(APIView):
    permission_classes = (AllowAny,)
    queryset = Users.objects.all()
    def post(self,request):
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ProductView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers