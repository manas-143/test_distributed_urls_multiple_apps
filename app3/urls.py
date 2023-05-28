from django.urls import path
from app3.views import *
app_name = "thing"
urlpatterns = [
    path('a3/', a3, name="a3"),
    path('aa3/', aa3, name="aa3"),
]
