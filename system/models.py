from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.

def uploaded_location(instance, filename):
    return ("%s/%s") %(instance.tên_xe,filename)
    
class Car(models.Model):
    hình_ảnh = models.ImageField(null=True, blank=True, upload_to='')
    tên_xe = models.CharField(max_length=100)
    tên_công_ty = models.CharField(max_length=100)
    số_ghế = models.IntegerField()
    giá = models.CharField(max_length=50)
    nội_dung = models.TextField()
    lượt_thích = models.IntegerField(default=0)

    def __str__(self):
        return self.tên_xe

    def get_absolute_url(self):
        return "/car/%s/" % (self.id)

class Order(models.Model):
    tên_xe = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='order')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    số_điện_thoại = models.CharField(max_length=15)
    địa_chỉ = models.TextField()
    ngày_đi = models.DateTimeField()
    ngày_về = models.DateTimeField()
    xuất_phát = models.CharField(max_length=100)
    điểm_đến = models.CharField(max_length=100)

    def __str__(self):
        return self.tên_xe

    def get_absolute_url(self):
        return "/car/detail/%s/" % (self.id)

class PrivateMsg(models.Model):
    tên_người_dùng = models.CharField(max_length=200)
    email = models.EmailField()
    nội_dung = models.TextField()

class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='history_user')
    tên_xe = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="history_ten_xe")

class Quote(models.Model):
    số_điện_thoại = models.CharField(max_length=15)
    tên_xe = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='quote')
    ngày_đi = models.DateTimeField()
    ngày_về = models.DateTimeField()
    xuất_phát = models.CharField(max_length=100)
    điểm_đến = models.CharField(max_length=100)
