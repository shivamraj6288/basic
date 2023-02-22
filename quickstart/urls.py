from django.urls import path, include
from .views import *

urlpatterns = [
    path("", Demo.as_view(), name="test")
]