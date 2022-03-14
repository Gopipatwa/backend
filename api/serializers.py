from rest_framework import serializers
from api.models import Product,Users


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['first_name','last_name','username','email','password','contact']

    def create(self,validated_data):
        print(validated_data,"_______________")
        password = validated_data.pop("password",None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class UserLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['username','password']

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
