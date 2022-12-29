"""Estore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from api.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cube',CubeView.as_view()),
    path('numcheck',Numcheck.as_view()),
    path('fact',Fact.as_view()),
    path('word',Wordcount.as_view()),
    path('pali',Pali.as_view()),
    path('arm',Armstrong.as_view()),
    path('prime',Prime.as_view()),
    path('products',Products.as_view()),
    path('morning', Morning.as_view()),
    path('add',Add.as_view()),
    path('mul',MUL.as_view()),
    path('sub',SUB.as_view()),
    path('books',Productview.as_view()),
    path('products/<int:id>',Productdetailsview.as_view()),
    path('reviews',ReviewsView.as_view()),
    path('reviews/<int:id>',ReviewDetails.as_view())

]
