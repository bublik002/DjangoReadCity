from django import forms
from django import forms
from .models import User, UserManager
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError




class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(label="Имя", min_length=3, max_length=20,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Фамилия", min_length=3, max_length=15,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label=' Почта', widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=100)
    password1 = forms.CharField(label='Пароль', max_length=100, min_length=5,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтвердите пароль', max_length=100, min_length=5,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_entry = forms.BooleanField(required=True, label='Согласие на обработку данных', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))

    class Meta:
        model = User  # Указываю какую модель использовать
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.EmailField(label='Почта',
                                widget=forms.TextInput(attrs={"autofocus": True, 'class': 'form-control'}))
    password = forms.CharField(label='Пароль', max_length=100, min_length=5,
                               widget=forms.TextInput(attrs={'class': 'form-control'}),
                               )
