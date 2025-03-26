from django import forms
from django import forms
from django.utils.translation import gettext_lazy as _

from .models import User, UserManager, BooksModel, CategoryModel
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

choices_cat = ((i.subcategory1 + ' / ' + i.subcategory2, i.subcategory1 + ' / ' + i.subcategory2) for i in
               CategoryModel.objects.all())
choices_age_rest = ((1, 'Нет'), (2, '6+'), (3, '12+'), (4, '16+'), (5, '18+'))


class CreateBooksForm(forms.Form):


    base_attrs = {'class': 'form-control'}


    title = forms.CharField(label=_('Название'), max_length=50,
                            widget=forms.TextInput(attrs=base_attrs))
    author = forms.CharField(label=_('Автор'), max_length=20,
                            widget=forms.TextInput(attrs=base_attrs))

    price = forms.IntegerField(label=_('Цена'),
                            widget=forms.TextInput(attrs=base_attrs))
    info_txt = forms.CharField(label=_('Описание'), max_length=1000,
                            widget=forms.TextInput(attrs=base_attrs))
    interpreter = forms.CharField(label=_('Переводчик'),
                            widget=forms.TextInput(attrs=base_attrs))

    publishing_house = forms.CharField(label=_('Издательство'),
                            widget=forms.TextInput(attrs=base_attrs))
    publishing_brand = forms.CharField(label=_('Издательский бренд'),
                            widget=forms.TextInput(attrs=base_attrs))
    series = forms.CharField(label=_('Серия'),
                            widget=forms.TextInput(attrs=base_attrs))  # Серия
    ISBN = forms.CharField(label='ISBN',
                            widget=forms.TextInput(attrs=base_attrs))
    num_page = forms.IntegerField(label=_('Количество страниц'),
                            widget=forms.TextInput(attrs=base_attrs))  # количество страниц
    size = forms.CharField(label=_('Размер'),
                            widget=forms.TextInput(attrs=base_attrs))  # размер
    cover_type = forms.CharField(label=_('Тип обложки'),
                            widget=forms.TextInput(base_attrs))  # Тип обложки
    circulation = forms.IntegerField(label=_('Тираж'),
                            widget=forms.TextInput(attrs=base_attrs))  # тираж
    # weight = forms.IntegerField(label=_('Вес'),
    #                         widget=forms.TextInput(attrs=base_attrs))  # вес
    # age_rest = forms.ChoiceField(label=_('Возрастные ограничения'), choices = choices_age_rest,
    #                         widget=forms.Select(attrs={'class': 'form-select', 'style':'width:10vw'}))  # возрастные ограничения
    #
    # img_local = forms.ImageField(label=_('Обложка'),required=False,
    #                           widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'file','id':'img_local'}))
    #
    #
    # cat = forms.ChoiceField(label="Категория", choices= choices_cat,
    #                         widget=forms.Select(attrs={'class': 'form-select', 'style':'width:25vw'}))




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
