from django import forms
from .models import Car, Order, PrivateMsg, Quote, Customer
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'

class DateForm(forms.Form):
    date_field = forms.DateField(widget=DateInput(format="%d-%m-%Y"))

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
            "danh_mục",
        ]
class OrderForm(forms.ModelForm):
    tên_khách_hàng = forms.CharField(max_length=50, required=False)
    ngày_đi = forms.DateField(widget=DateInput(format="%d-%m-%Y"), help_text="Ví dụ: tháng / ngày / năm")
    ngày_về = forms.DateField(widget=DateInput(format="%d-%m-%Y"), help_text="Ví dụ: tháng / ngày / năm")
    xuất_phát = forms.CharField(required=True)
    điểm_đến = forms.CharField(required=True)

    class Meta:
        model = Order
        fields = [
            "tên_xe",
            "tên_khách_hàng",
            "email",
            "ngày_đi","ngày_về",
            "xuất_phát",
            "điểm_đến",
            "nhu_cầu_khác"
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
    ngày_đi = forms.DateField(widget=DateInput(format="%d-%m-%Y"), help_text="Ví dụ: tháng / ngày / năm")
    ngày_về = forms.DateField(widget=DateInput(format="%d-%m-%Y"), help_text="Ví dụ: tháng / ngày / năm")
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
    số_điện_thoại = forms.IntegerField()
    địa_chỉ = forms.CharField()

    class Meta:
        model = Customer
        fields = [
            "số_điện_thoại",
            "địa_chỉ",
        ]