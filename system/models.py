from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.conf import settings

# Create your models here.

def uploaded_location(instance, filename):
    return ("%s/%s") %(instance.tên_xe,filename)
    
class Car(models.Model):
    hình_ảnh = models.ImageField(null=True, blank=True, upload_to='')
    tên_xe = models.CharField(max_length=100)
    tên_công_ty = models.CharField(max_length=100)
    số_ghế = models.IntegerField()
    giá_tham_khảo = models.FloatField(max_length=50)
    nội_dung = models.TextField()
    lượt_thích = models.IntegerField(default=0)

    def __str__(self):
        return self.tên_xe

    def get_absolute_url(self):
        return "/car/%s/" % (self.id)

class Quote(models.Model):
    số_điện_thoại = models.CharField(max_length=15)
    tên_xe = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='quote_xe')
    ngày_đi = models.DateTimeField()
    ngày_về = models.DateTimeField()
    xuất_phát = models.CharField(max_length=100)
    điểm_đến = models.CharField(max_length=100)

class Customer(models.Model):
    tên_khách_hàng = models.CharField(max_length=100)
    số_điện_thoại = models.IntegerField()
    địa_chỉ = models.TextField()

    def __str__(self):
        return str(self.tên_khách_hàng)

class PrivateMsg(models.Model):
    tên_người_dùng = models.CharField(max_length=100)
    email = models.EmailField()
    số_điện_thoại = models.IntegerField(default=0000000000)
    nội_dung = models.TextField()

    def __str__(self):
        return str(self.user.first_name)

class Order(models.Model):
    tên_xe = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='order')
    user = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order_customer', null=True, blank=True)
    tên_khách_hàng = models.CharField(max_length=255)
    ngày_đi = models.DateTimeField()
    ngày_về = models.DateTimeField()
    xuất_phát = models.CharField(max_length=100)
    điểm_đến = models.CharField(max_length=100)

    def __str__(self):
        return self.tên_xe

    def get_absolute_url(self):
        return "/car/detail/%s/" % (self.id)