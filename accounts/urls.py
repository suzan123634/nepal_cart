from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
   path('', views.user_register, name='signup'),
   path('logout/',views.logout_user,name='logout'),
   path('login/',views.login_user,name='login')
]
