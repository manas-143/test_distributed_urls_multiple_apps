from django.urls import path
from app1.views import *
app_name = "something"
urlpatterns = [
    path('a1/', a1, name="a1"),
    path('aa1/', aa1, name="aa1"),
]
