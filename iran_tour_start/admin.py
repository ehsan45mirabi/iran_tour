from django.contrib import admin
from .models import card_tour, Person, Category
# Register your models here.

admin.site.register(card_tour)
admin.site.register(Person)
admin.site.register(Category)