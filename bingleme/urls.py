"""bingleme URL Configuration

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
from django.urls import path
from django.conf.urls import url
from . import view
urlpatterns = [
    url(r'^$', view.index),
    url(r'^cart$', view.cart),
    url(r'^category$', view.category),
    url(r'^delete$', view.delete),
    url(r'^grounding$', view.grounding),
    url(r'^order_history$', view.order_history),
    url(r'^order_information$', view.order_information),
    url(r'^quickview$', view.quickview),
    url(r'^register$', view.register),
    url(r'^login$', view.login)
]
