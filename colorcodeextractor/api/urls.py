from django.urls import path
from .views import *

urlpatterns = [
    path('upload_image/', upload_image, name='upload_image'), #url to upload image
    path('register/', register_user, name='register_user'), #register user url
    path('login/', user_login, name='login'), # Login user url
    path('logout/', user_logout, name = 'logout'), # Logout user url
]
