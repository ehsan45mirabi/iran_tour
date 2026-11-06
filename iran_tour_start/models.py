from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Person(AbstractUser):
    phone = models.CharField(max_length=127, null=True, blank=True)
    GENDER = {
        '0': 'male',
        '1': 'femaie',
    }
    gender = models.CharField(
        max_length=1, choices=GENDER, null=True, default='0')
    external_id = models.CharField(max_length=127, null=True, blank=True)


class Category(models.Model):
    title = models.CharField(max_length=128, null=True)

    def __str__(self):
        return self.title
    
class card_tour(models.Model):
    title = models.CharField(max_length=128, null=True, verbose_name='عنوان')
    title_details = models.CharField(max_length=300, null=True, verbose_name='عنوان صفحه گردشگری')
    image = models.TextField(max_length=2026, null=True, blank=True, verbose_name='عکس')
    image_2 = models.TextField(max_length=2026, null=True, blank=True, verbose_name='عکس صفحه گردشگری')
    descriptions = models.TextField(max_length=2026, null=True, blank=True, verbose_name='توضیحات')
    trait_1 = models.CharField(max_length=300, null=True, blank=True, verbose_name='دلیل اول ')
    trait_2 = models.CharField(max_length=300, null=True, blank=True, verbose_name='دلیل دوم ')
    trait_3 = models.CharField(max_length=300, null=True, blank=True, verbose_name='دلیل سوم')
    trait_4 = models.CharField(max_length=300, null=True, blank=True, verbose_name='دلیل چهارم')
    city = models.ForeignKey(Category,on_delete=models.SET_NULL, null=True, blank=True, verbose_name='شهر ')
    map_locations = models.TextField(max_length=2001, null=True, verbose_name='محل قرار دادن لوکیشن')

    def __str__(self):
        return self.title