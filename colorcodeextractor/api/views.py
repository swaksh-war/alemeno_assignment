from django.core.files.uploadedfile import UploadedFile
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.decorators import api_view, parser_classes, permission_classes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

import cv2
import numpy as np

from . import utils
from .serializers import UserSerializer
from .models import CustomUser



@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def upload_image(request):
    '''
    This api method handles uploading images and storing the metadata in the sqlite3.
    Also it stores the uploaded image in a local container inside Media folder.
    '''
    if request.method == "POST":
        image_file : UploadedFile = request.data.get('image')
        image_data = image_file.read()
        image_np_data = np.frombuffer(image_data, np.uint8)
        img_cv2 = cv2.imdecode(image_np_data, cv2.IMREAD_COLOR)
        color_codes = utils.extract_colors(img_cv2)
        response = Response({"color_codes" : color_codes}, status= HTTP_200_OK)
        return response
    return Response({"message" : "error"}, status = HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["POST"])
def register_user(request):
    '''
    User Registration method using api
    '''
    if request.method == "POST":
        if not request.data:
            return Response({"detail": "No data Provided"}, status = HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass
        
        if not user:
            user = authenticate(username=username, password=password)
        
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token' : token.key}, status=HTTP_200_OK)
        return Response({'error': 'Invalid Credentials'}, status=HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({'message' : 'You are successfully logged out'}, status=HTTP_200_OK)
    return Response({'message' : 'Error while logging out'}, status=HTTP_500_INTERNAL_SERVER_ERROR)