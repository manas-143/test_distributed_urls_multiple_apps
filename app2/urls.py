from django.urls import path
from app2.views import *
app_name = "anything"
urlpatterns = [
    path('a2/', a2, name="a2"),
    path('aa2/', aa2, name="aa2"),
]