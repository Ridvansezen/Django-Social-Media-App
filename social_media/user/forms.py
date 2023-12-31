from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(label="Kullanıcı adı", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Parola", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı adı")
    password = forms.CharField(max_length=50,label="Parola", widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=50, label="Parolayı doğrulayın", widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Parolalar eşleşmiyor...")
        
        
        values = {
            "username":username,
            "password":password
        }

        return values
    
class ChangeUsernameForm(forms.Form):
    new_username = forms.CharField(label="Yeni Kullanıcı adı", max_length=50)

    def clean_new_username(self):
        new_username = self.cleaned_data['new_username']
        # Yeni kullanıcı adının kullanılabilir olduğunu kontrol edin
        if User.objects.filter(username=new_username).exists():
            raise forms.ValidationError('Bu kullanıcı adı zaten kullanılıyor.')
        return new_username
    
class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(label="Yeni Parola", max_length=100, widget=forms.PasswordInput)

