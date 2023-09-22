from django.core.files.uploadedfile import UploadedFile

from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.parsers import MultiPartParser, FormParser

import cv2
import numpy as np

from . import utils
from .serializers import UploadedPhotoSerializer
# Create your views here.

@api_view(["POST"])
@parser_classes([MultiPartParser, FormParser])
def upload_image(request):
    if request.method == "POST":
        image_file : UploadedFile = request.data.get('image')
        image_data = image_file.read()
        image_np_data = np.frombuffer(image_data, np.uint8)
        img_cv2 = cv2.imdecode(image_np_data, cv2.IMREAD_COLOR)
        color_codes = utils.extract_colors(img_cv2)
        serializer = UploadedPhotoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        response = Response({"color_codes" : color_codes, "serializer-data" : serializer.data}, status= HTTP_200_OK)
        return response
    return Response({"message" : "error"}, status = HTTP_500_INTERNAL_SERVER_ERROR)

