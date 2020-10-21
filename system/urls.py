from django.urls import path, include
from django.contrib import admin
from system.views import (
    home,
    car_list,
    order_created,
    car_update,
    car_detail,
    order_detail,
    order_created2,
    car_delete,
    order_delete,
    contact,
    newcar,
    like_update,
    popular_car,
    quote,
    customer_profile,
    profile_update,
    blog_list,
    blog_created,
    blog_update,
    blog_delete,
    blog_detail,
)

urlpatterns = [
    path("carlist/", car_list, name="car_list"),
    path("createOrder", order_created2, name="order_create"),
    path("createOrder/<car_id>", order_created, name="order_creates"),
    path("(<id>)/edit/", car_update, name="car_edit"),
    path("(<id>)/", car_detail, name="car_detail"),
    path("detail/<id>/", order_detail, name="order_detail"),
    path("(<id>)/delete/", car_delete, name="car_delete"),
    path("(<id>)/deleteOrder/", order_delete, name="order_delete"),
    path("contact/", contact, name="contact"),
    path("newcar/", newcar, name="newcar"),
    path("(<id>)/lượt_thích/", like_update, name="lượt_thích"),
    path("popularcar/", popular_car, name="popularcar"),
    path("quote/", quote, name="quote"),
    path("update/", profile_update, name="update_customer"),
    # ---------------Blog----------------
    path("bloglist/", blog_list, name="blog_list"),
    path("blog/(<id>)/", blog_detail, name="blog_detail"),
    path("newblog/", blog_created, name="newblog"),
    path("blog/(<id>)/edit/", blog_update, name="blog_edit"),
    path("(<id>)/delete/", blog_delete, name="blog_delete"),
]
