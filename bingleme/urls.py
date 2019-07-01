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
from . import view,user_register,user_login,search_medicine,classify_medicine,cart_show,\
    cart_update,cart_add,cart_remove,admin_index,admin_search,edit_medicine,admin_orderlist
urlpatterns = [
    url(r'^$', view.index),
    url(r'^index$', view.index),
    url(r'^cart$', cart_show.cart_show),
    url(r'^category$', view.category),
    url(r'^grounding$', view.grounding),
    url(r'^order_history$', view.order_history),
    url(r'^order_information/$', view.order_information),
    url(r'^quickview/$', view.quickview),
    url(r'^register$', view.register),
    url(r'^login$', view.login),
    url(r'^product/$', view.product),
    url(r'^user_register$', user_register.user_register),
    url(r'^user_login$', user_login.user_login),
    url(r'^search_medicine$', search_medicine.search_medicine),
    url(r'^loginOut$', view.loginOut),
    url(r'^classify_medicine/$', classify_medicine.classify_medicine),
    url(r'^arrive/$', view.hasArrive),
    url(r'^pay/$', view.pay),
    url(r'^newOrder$',view.newOrder),
    url(r'^cart_update$', cart_update.cart_update),
    url(r'^cart_add$', cart_add.cart_add),
    url(r'^cart_remove/$',cart_remove.cart_remove),
    url(r'^medicine_list/$', view.medicine_list),
    url(r'^admin$', admin_index.adminIndex),
    url(r'^admin_search/$',admin_search.admin_search),
    url(r'^edit_medicine/$', edit_medicine.edit_medicine),
    url(r'^delete_image/$', view.delete_image),
    url(r'^admin_orderlist$', admin_orderlist.getAdminOrder),

]
