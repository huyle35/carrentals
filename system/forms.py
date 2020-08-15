from django import forms
from .models import Car, Order, PrivateMsg, History, Quote
from django.contrib.auth.models import User

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "hình_ảnh",
            "tên_xe",
            "tên_công_ty",
            "số_ghế",
            "giá",
            "nội_dung",
        ]
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "tên_xe",
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
