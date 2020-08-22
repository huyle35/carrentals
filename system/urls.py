from django.urls import path, include
from django.contrib import admin
from system.views import (home, car_list, order_created, car_update, car_detail, order_detail, 
car_delete, order_delete, contact, newcar, like_update, popular_car, quote, customer_profile, 
profile_update, CategoryView)

urlpatterns = [
    path('carlist/', car_list, name = "car_list"),
    path('createOrder/', order_created, name = "order_create"),

    path('(<id>)/edit/', car_update, name = "car_edit"),

    path('(<id>)/', car_detail, name = "car_detail"),
    path('detail/<id>/', order_detail, name = "order_detail"),

    path('(<id>)/delete/', car_delete, name = "car_delete"),
    path('(<id>)/deleteOrder/', order_delete, name = "order_delete"),

    path('contact/', contact, name = "contact"),

    path('newcar/', newcar, name = "newcar"),
    path('(<id>)/lượt_thích/', like_update, name = "lượt_thích"),
    path('popularcar/', popular_car, name = "popularcar"),
    path('quote/', quote, name = "quote"),

    path('update/', profile_update, name = "update_customer"),
    path('category/', CategoryView.as_view(), name = "category"),

]
