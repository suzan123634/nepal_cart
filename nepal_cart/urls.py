"""nepal_cart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.static import serve
from django.contrib.admin import AdminSite

AdminSite.site_header = "Nepal_Cart"
AdminSite.site_title = "Nepal_Cart title"
AdminSite.index_title = "Nepal_Cart title"


urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('search', views.search, name='search'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('boy/', views.boy, name='boy'),
    path('boys/', views.boys, name='boys'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('girl/', views.girl, name='girl'),
    path('girls/', views.girls, name='girls'),
    path('men/', views.men, name='men'),
    path('mens/', views.mens, name='mens'),
    path('payment/', views.payment, name='payment'),
    path('shop/', views.shop, name='shop'),
    path('single/', views.single, name='single'),
    path('women/', views.women, name='women'),
    path('womens/', views.womens, name='womens'),
    path('', include('accounts.urls')),
]
