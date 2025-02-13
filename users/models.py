from django.db import models
from django.contrib.auth.models import AbstractUser
from django.fields import CountryField


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True, verbose_name='Email', help_text='Укажите Вашу почту')
    avatar = models.ImageField(upload_to='users/avatar/', verbose_name='Аватар', blank=True, null=True, help_text='Загрузите свой аватар')
    phone = models.CharField(max_length=12, verbose_name='Телефон', blank=True, null=True, help_text='Введите номер телефона')
    country = CountryField(max_length=100, verbose_name='Страна')
