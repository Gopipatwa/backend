# from django.shortcuts import render
from email.policy import HTTP
from api.serializers import UserSerializers,UserLoginSerializers,ProductSerializers
from api.models import Users,Product
from django.contrib.auth import authenticate
from django.http import Http404
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
        'Detail View':'/product/<int:pk>/',
        'Login':'/login/',
        'Register':'/register/'}
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
            return Response({'message':"success","username":username,"password":psd},status=status.HTTP_200_OK)
        else:
            return Response({"message":"invalid authenticate"},status=status.HTTP_401_UNAUTHORIZED)

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


# class ProductView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers

class ProductView(APIView):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    def get(self, request, format=None):
        product = Product.objects.all()
        serializer = ProductSerializers(product, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductSerializers(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response({"message":"success"},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializers(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)