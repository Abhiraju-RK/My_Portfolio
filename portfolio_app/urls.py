from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('download_resume', views.download_resume, name='download_resume'),
]