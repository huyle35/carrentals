from django import forms
from django.utils import timezone
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,

)
User = get_user_model()
import re
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, help_text='Vui lòng nhập Email hợp lệ.')
    birth_date = forms.DateField(required=False, help_text='Vui lòng nhập theo Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2', )

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error('confirm_password', "Xác nhận mật khẩu không đúng. Vui lòng nhập lại !")

        return cleaned_data

    def clean_username(self):

        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Tên tài khoản có kí tự đặc biệt")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Tài khoản đã tồn tại")


    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit)
        user.last_login = timezone.now()
        if commit:
            user.save()
        return user
        
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Tài khoản không tồn tại hoặc sai mật khẩu. Vui lòng nhập lại !")
            if not user.is_active:
                raise forms.ValidationError("Tài khoản không còn hoạt động. Vui lòng đăng ký tài khoản mới !")
        return super(UserLoginForm,self).clean(*args, **kwargs)

