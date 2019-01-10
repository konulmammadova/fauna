from django import forms

from base_user.models import MyUser
from fauna_app.models import Appointment, Service


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name', 'phone', 'service_type', 'email', 'pet_category', 'visiting_date', 'message']
        # widgets = {
        #     'service_type': forms.Select(attrs={'class': "select-input", 'name': "category"}),
        #     # 'pet_category': forms.Select(attrs={'class': "select-input", 'name': "category"}),
        #     'visiting_date': forms.DateInput(
        #         attrs={'class': 'datepicker', 'name': "date", 'placeholder': "Görüş Tarixi"}),
        # }


class RegisterForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
