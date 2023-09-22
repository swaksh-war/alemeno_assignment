from django.core.files.uploadedfile import UploadedFile

from rest_framework.serializers import ModelSerializer

from .models import CustomUser


class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password' : {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(username = validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    


