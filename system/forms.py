from django import forms
from .models import Car, Order, PrivateMsg, Quote, Customer
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
    ngày_đi = forms.DateField(required=True)
    ngày_về = forms.DateField(required=True)
    xuất_phát = forms.CharField(required=True)
    điểm_đến = forms.CharField(required=True)

    class Meta:
        model = Order
        fields = [
            "tên_xe",
            "tên_khách_hàng",
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
            "số_điện_thoại",
            "email",
            "nội_dung",
        ]

class QuoteForm(forms.ModelForm):
    số_điện_thoại = forms.IntegerField(required=True)
    ngày_đi = forms.DateField(required=True, help_text="Ví dụ: 01/01/2020")
    ngày_về = forms.DateField(required=True, help_text="Ví dụ: 01/01/2020")
    xuất_phát = forms.CharField(required=True)
    điểm_đến = forms.CharField(required=True)

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

class ProfileForm(forms.ModelForm):
    tên_khách_hàng = forms.CharField()
    số_điện_thoại = forms.IntegerField()
    địa_chỉ = forms.CharField()

    class Meta:
        model = Customer
        fields = [
            "tên_khách_hàng",
            "số_điện_thoại",
            "địa_chỉ",
        ]