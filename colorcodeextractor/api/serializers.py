from django.core.files.uploadedfile import UploadedFile

from rest_framework.serializers import ModelSerializer

from .models import UploadedPhoto


class UploadedPhotoSerializer(ModelSerializer):
    class Meta:
        model = UploadedPhoto
        fields = '__all__'

    def create(self, validated_data):
        uploaded_file : UploadedFile = validated_data['image']
        filename = uploaded_file.name()
        image_ins = UploadedPhoto(name = filename, file = uploaded_file)
        image_ins.save()
        return image_ins

