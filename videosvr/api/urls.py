from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import *

app_name = 'users'

urlpatterns = [
    url(r'^login/', UserLoginApiView.as_view(), name='login'),
    url(r'^upload-video/', UploadVideo.as_view(), name='upload-video'),
    url(r'^download-video/', download_video, name='download-video'),

    ]