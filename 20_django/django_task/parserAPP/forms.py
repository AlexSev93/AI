from django import forms
from .models import Vacancies


# class Request(forms.Form):
#     vacancy = forms.CharField(label='Вакансия',
#                               widget=forms.TextInput(attrs={'placeholder': 'Название вакансии', 'class': 'form-control'}))
#     region = forms.CharField(label='Страна',
#                              widget=forms.TextInput(attrs={'placeholder': 'Страна поиска', 'class': 'form-control'}))
#
#     select = [(i+1, (i+1)*20) for i in range(4)]
#     pages = forms.ChoiceField(label='Количество вакансий',
#                               widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), choices=select)


# постройка формы по модели
class Request(forms.ModelForm):
    vacancy = forms.CharField(label='Вакансия',
                              widget=forms.TextInput(attrs={'placeholder': 'Название вакансии', 'class': 'form-control'}))
    regions = forms.CharField(label='Страна',
                             widget=forms.TextInput(attrs={'placeholder': 'Страна поиска', 'class': 'form-control'}))

    select = [(i+1, (i+1)*20) for i in range(4)]
    pages = forms.ChoiceField(label='Количество вакансий',
                              widget=forms.RadioSelect(attrs={'class': 'form-check-inline'}), choices=select)
    class Meta:
        model = Vacancies
        exclude = ('image', 'words')
