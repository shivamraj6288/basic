from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class Demo(APIView):
    def get(self, request, format=None):
        return Response({"message":"server is working"}, status=status.HTTP_200_OK)

