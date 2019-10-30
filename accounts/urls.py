from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
   path('signup', views.user_register, name='accounts/singup')
]
