"""
This is views file of api module app.
@author anshul guppta
"""

import os
import mimetypes

from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import StreamingHttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from wsgiref.util import FileWrapper

from .models import User

class  UserLoginApiView( APIView):
	"""
	    @author: Anshul Gupta, anshulgupta217@gmail.com

	    @request: ['POST',]
	    {"email":"anshulgupta217@gmail.com","password":"python@123"
	    @response: [200, 402]
		{"token":"skdfjn7foijw923hd9032d23","message":"invalid credentials"}
	    @summary: Used for user-login  

	"""
	authentication_classes = []

	def post(self, request):
		data = request.data #json data received in post request
		"""
		check for two fields in request can also be checked using serializer.
		"""
		if "email" not in data:
			return Response({"message":"email field missing"}, status=402)
		
		if "password" not in data:
			return Response({"message":"password field missing"}, status=402)
		
		user = authenticate(username=data["email"], password=data["password"]) # django auth function for verifying creds
		if user is None:
		    return Response({"message":"invalid credentials"})
		else:
		    response = {
		        'auth_token': Token.objects.get_or_create(user=user)[0].key,
		        'message':"successfully logined"
		    }
		    return Response(response, 200)


class UploadVideo(APIView):
	"""
	    @author: Anshul Gupta, anshulgupta217@gmail.com

	    @request: ['POST',]
	    request type multipart
	    file key name should be video
	    @response: [200]
		{"url":"media/VID-20171012-WA0004_yJvXe7u.mp4"}
	    @summary: Use post request to upload video 

	"""
	def post(self, request):
		myfile = request.FILES['video'] # accessing video from the file request
		fs = FileSystemStorage() #django file storage to get instance of file system
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		return Response({"url":uploaded_file_url}, status=200)




def download_video(request):
   file_ = os.getcwd()+'/media/abc.webm'  #setting file from the server to serve
   filename = os.path.basename(the_file)
   chunk_size = 500 #setting up chunks
   response = StreamingHttpResponse(FileWrapper(open(file_, 'rb'), chunk_size),
                           content_type=mimetypes.guess_type(file_)[0])
   response['Content-Length'] = os.path.getsize(file_)    
   response['Content-Disposition'] = "attachment; filename=%s" % filename
   return response