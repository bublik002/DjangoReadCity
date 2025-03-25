from __future__ import unicode_literals
from pytils.translit import slugify
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from googletrans import Translator, constants
from pprint import pprint

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not email:
            raise ValueError('email должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_stuff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CategoryModel(models.Model):

    subcategory1 = models.CharField(max_length=100, blank=True)
    subcategory2 = models.CharField(max_length=100, blank=True)

    sub_slugify1 = models.CharField(blank=True, max_length=500)
    sub_slugify2 = models.CharField(blank=True, max_length=500)


    class Meta:
        app_label = 'main'


    def __str__(self):
        return f'({self.subcategory1}) ({self.subcategory2})'

    def save(self, *args, **kwargs):
        self.sub_slugify1 = slugify(self.subcategory1)
        self.sub_slugify2 = slugify(self.subcategory2)
        super(CategoryModel, self).save(*args, **kwargs)


class ReviewsModel(models.Model):
    user_name = models.ForeignKey('User', on_delete=models.PROTECT, related_name='review_user')
    score = models.IntegerField()
    date = models.DateField(auto_now_add=True)
    comment = models.CharField(max_length=200)
    book = models.ForeignKey('BooksModel', null=True, blank=True, related_name='review', on_delete=models.CASCADE)

    pluses = models.CharField(max_length=200, blank=True)
    minuses = models.CharField(max_length=200, blank=True)


class BooksModel(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(blank=True, max_length=100)
    img = models.CharField(max_length=300, blank=True)

    img_local = models.FileField(upload_to='cover', blank=True)

    price = models.IntegerField()
    info_txt = models.CharField(max_length=4000)
    slug_title = models.CharField(blank=True, max_length=500)

    category = models.ManyToManyField(CategoryModel)

    interpreter = models.CharField(blank=True, max_length=100)
    id_book = models.IntegerField(null=True, blank=True)  # id
    publishing_house = models.CharField(blank=True, max_length=100)
    publishing_brand = models.CharField(blank=True, max_length=100)
    series = models.CharField(max_length=100, blank=True)  # Серия
    year_of_publishing = models.IntegerField(blank=True, null=True)  # год публикации
    ISBN = models.CharField(max_length=100, blank=True)
    num_page = models.IntegerField(blank=True)  # количество страниц
    size = models.CharField(max_length=100)  # размер
    cover_type = models.CharField(max_length=100)  # Тип обложки
    circulation = models.IntegerField(blank=True, null=True)  # тираж
    weight = models.IntegerField(blank=True)  # вес

    publishing = models.BooleanField(default=False)

    age_rest = models.CharField(choices=(('1', 'Нет'), ('2', '6+'), ('3', '12+'), ('4', '16+'), ('5', '18+') ), default='1', blank=True)
    # age_rest = models.IntegerField(blank=True, null=True)  # возрастные ограничения

    creator = models.ForeignKey('User', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug_title = slugify(self.title)

        # self.title_en = наш перевод
        super(BooksModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


# f4beKE9-Kaw sscorpionmuz969@gmail.com
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('name'), max_length=30, blank=True)
    last_name = models.CharField(_('surname'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('registered'), auto_now_add=True)
    is_active = models.BooleanField(_('is_active'), default=True)  # Активный пользователь
    is_staff = models.BooleanField('is_stuff', default=True)  # Может войти в admin login
    phone_number = models.CharField(max_length=12, default='77777777777')

    seller = models.BooleanField(default=False)

    bookmarks = models.ManyToManyField(BooksModel, blank=True, related_name='bookmarks')
    basket = models.ManyToManyField(BooksModel, blank=True, related_name='basket')
    objects = UserManager()

    viewed = models.ManyToManyField(BooksModel, blank=True, related_name='viewed', max_length=50)

    USERNAME_FIELD = 'email'  # Авторизация по email
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Возвращает first_name и last_name с пробелом между ними.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Возвращает сокращенное имя пользователя.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Отправляет электронное письмо этому пользователю.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)
