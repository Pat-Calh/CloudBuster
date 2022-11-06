"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .views import Home, AccountHandler, Account, ManageHandler, ManageStock, Manage, CheckoutHandler, Checkout

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("", Home.as_view()),
    path("home/", Home.as_view()),
    path("accountHandler/", AccountHandler.as_view()),
    path("account/", Account.as_view()),
    path("manageHandler/", ManageHandler.as_view()),
    path("manageStock/", ManageStock.as_view()),
    path("manage/", Manage.as_view()),
    path("checkoutHandler/", CheckoutHandler.as_view()),
    path("checkout/", Checkout.as_view())  
]