from django import forms
from django.core.validators import MinValueValidator,MaxValueValidator


class Request(forms.Form):
    vacancy = forms.CharField(label='Вакансия')
    region = forms.CharField(label='Страна')
    pages = forms.IntegerField(label='Количество страниц', min_value=1, max_value=5)
