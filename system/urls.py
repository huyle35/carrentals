from django.conf.urls import url
from django.contrib import admin
from system.views import home, car_list, order_created, car_update, car_detail, order_detail, car_delete, order_delete, contact, newcar, like_update, popular_car

urlpatterns = [
    url(r'^$', home, name = "home"),

    url(r'^carlist/$', car_list, name = "car_list"),
    url(r'^createOrder/$', order_created, name = "order_create"),

    url(r'^(?P<id>\d+)/edit/$', car_update, name = "car_edit"),

    url(r'^(?P<id>\d+)/$', car_detail, name = "car_detail"),
    url(r'^detail/(?P<id>\d+)/$', order_detail, name = "order_detail"),

    url(r'^(?P<id>\d+)/delete/$', car_delete, name = "car_delete"),
    url(r'^(?P<id>\d+)/deleteOrder/$', order_delete, name = "order_delete"),

    url(r'^contact/$', contact, name = "contact"),

    url(r'^newcar/$', newcar, name = "newcar"),
    url(r'^(?P<id>\d+)/like/$', like_update, name = "like"),
    url(r'^popularcar/$', popular_car, name = "popularcar"),

]
