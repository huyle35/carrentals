from django import forms
from .models import Car, Order, PrivateMsg, History, Quote
from django.contrib.auth.models import User

class CarForm(forms.ModelForm):
    tên_xe = forms.CharField(required=True)
    tên_công_ty = forms.CharField(required=False)
    số_ghế = forms.IntegerField(required=True)
    giá_tham_khảo = forms.FloatField(required=True)

    class Meta:
        model = Car
        fields = [
            "hình_ảnh",
            "tên_xe",
            "tên_công_ty",
            "số_ghế",
            "giá_tham_khảo",
            "nội_dung",
        ]
class OrderForm(forms.ModelForm):
    tên_khách_hàng = forms.CharField(max_length=50, required=False)
    số_điện_thoại = forms.CharField(required=True)
    địa_chỉ = forms.CharField(required=False)
    ngày_đi = forms.DateField(required=True)
    ngày_về = forms.DateField(required=True)
    xuất_phát = forms.CharField(required=True)
    điểm_đến = forms.CharField(required=True)

    class Meta:
        model = Order
        fields = [
            "tên_xe",
            "tên_khách_hàng",
            "số_điện_thoại",
            "địa_chỉ",
            "ngày_đi",
            "ngày_về",
            "xuất_phát",
            "điểm_đến",
        ]
class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMsg
        fields = [
            "tên_người_dùng",
            "email",
            "nội_dung",
        ]

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = [
            "user",
            "tên_xe",
        ]

class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = [
            "số_điện_thoại",
            "tên_xe",
            "ngày_đi",
            "ngày_về",
            "xuất_phát",
            "điểm_đến",
        ]
