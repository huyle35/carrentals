 # -*- coding: utf-8 -*
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
    status = forms.BooleanField(required=False)

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
            "status"
        ]
        
class OrderForm(forms.ModelForm):
    # tên_xe = forms.IntegerField(widget=forms.HiddenInput(), initial=1)
    defaultcar = Car.objects.get(id=1)
    # # form = OrderForm(initial={''})
    CHOICES = [('1',Car.objects.get(id=1).tên_xe), 
                ('34',Car.objects.get(id=34).tên_xe),
                ('35',Car.objects.get(id=35).tên_xe),
                ('36',Car.objects.get(id=36).tên_xe),
                ('37',Car.objects.get(id=37).tên_xe),
                ('40',Car.objects.get(id=40).tên_xe),
                ('41',Car.objects.get(id=41).tên_xe),
                ('42',Car.objects.get(id=42).tên_xe),
                ('43',Car.objects.get(id=43).tên_xe),
                ('44',Car.objects.get(id=44).tên_xe),
                ('45',Car.objects.get(id=45).tên_xe),
                ('46',Car.objects.get(id=46).tên_xe)]
    title_xe = forms.ChoiceField(choices=CHOICES)
    
    tilte_xe.choices = CHOICES    
    tên_xe = Car.objects.get(id=1)
    tên_khách_hàng = forms.CharField(max_length=50, required=False)
    ngày_đi = forms.DateField(widget=DateInput(format="%d-%m-%Y"), help_text="Ví dụ: tháng / ngày / năm")
    ngày_về = forms.DateField(widget=DateInput(format="%d-%m-%Y"), help_text="Ví dụ: tháng / ngày / năm")
    xuất_phát = forms.CharField(required=True)
    điểm_đến = forms.CharField(required=True)

    class Meta:
        model = Order
        fields = [
            "title_xe",
            "tên_khách_hàng",
            "email",
            "ngày_đi",
            "ngày_về",
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
            "email",
            "ngày_đi",
            "ngày_về",
            "xuất_phát",
            "điểm_đến",
            "nhu_cầu_khác",
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