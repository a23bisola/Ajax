from django.urls import path
from. import views



urlpatterns=[
path('', views.home, name='home'),
path('creat', views.homecreate, name='creat'),
path('getprofiles', views.getprofiles, name='getprofiles'),
path('create', views.createprofile, name='create')
]
