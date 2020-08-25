from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.conf import settings
from django.shortcuts import reverse


# Create your models here.

def uploaded_location(instance, filename):
    return ("%s/%s") %(instance.tên_xe,filename)

class Category(models.Model):
    danh_mục = models.CharField(max_length=100)
    mô_tả = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.danh_mục

 
class Car(models.Model):
    hình_ảnh = models.ImageField(null=True, blank=True, upload_to='')
    danh_mục = models.ForeignKey(Category, on_delete=models.CASCADE)
    tên_xe = models.CharField(max_length=100)
    tên_công_ty = models.CharField(max_length=100)
    số_ghế = models.IntegerField()
    giá_tham_khảo = models.FloatField(max_length=50)
    nội_dung = models.TextField()
    lượt_thích = models.IntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.tên_xe

    def get_absolute_url(self):
        return "/car/%s/" % (self.id)
    
class Quote(models.Model):
    số_điện_thoại = models.CharField(max_length=12)
    tên_xe = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='quote_xe')
    email = models.EmailField()
    ngày_đi = models.DateField()
    ngày_về = models.DateField()
    xuất_phát = models.CharField(max_length=100)
    điểm_đến = models.CharField(max_length=100)
    nhu_cầu_khác = models.CharField(max_length=255, blank=True, null=True)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='customer', null=True, blank=True)
    số_điện_thoại = models.CharField(max_length=12)
    địa_chỉ = models.TextField()

    def __str__(self):
        return str(self.user.id)

class PrivateMsg(models.Model):
    tên_người_dùng = models.CharField(max_length=100)
    email = models.EmailField()
    số_điện_thoại = models.CharField(max_length=12)
    nội_dung = models.TextField()

    def __str__(self):
        return str(self.tên_người_dùng)

class Order(models.Model):
    title_xe = models.IntegerField()
    tên_xe = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='order')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    tên_khách_hàng = models.CharField(max_length=255)
    email = models.EmailField()
    ngày_đi = models.DateField()
    ngày_về = models.DateField()
    xuất_phát = models.CharField(max_length=100)
    điểm_đến = models.CharField(max_length=100)
    nhu_cầu_khác = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.tên_xe

    def get_absolute_url(self):
        return "/car/detail/%s/" % (self.id)