from django import forms
from django.contrib.auth.models import User
from account.models import UserInFo


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}), )
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    # def clean_email(self):
    #     cd = self.cleaned_data
    #     if cd.__len__() < 8:
    #         raise forms.ValidationError(u"请输入至少8位密码")
    #     return cd['email']


class SetPasswordForm(forms.Form):
    old_password = forms.CharField(label="旧密码", max_length=256,
                                   widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label="新密码", max_length=256,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="确认新密码", max_length=256,
                                    widget=forms.PasswordInput(attrs={'class': 'form-control'}))


# class UserInFoForm(forms.ModelForm):
#     class Meta:
#         model = UserInFo
#         fields = ('age', 'profession', 'hobby', 'phone', 'weiChat', 'skills')
