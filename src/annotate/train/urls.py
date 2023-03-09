#from django.conf.urls import url
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('api/getImage', views.getImage),
    path('annotate', views.annotate)
]
