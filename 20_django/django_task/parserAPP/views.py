from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Vacancies, Regions
from .forms import Request
from .management.commands.fill_db import Command
import pprint


# Create your views here.
def main_view(request):
    vacancies = Vacancies.objects.all()
    region = Regions.objects.all()

    return render(request, 'parserAPP/index.html',
                  context={'vacancies': vacancies, 'region': region})


def request_vacancy(request):
    if request.method == 'POST':
        form = Request(request.POST)
        if form.is_valid():
            country = form.cleaned_data['region']
            name_vacancy = form.cleaned_data['vacancy']
            pages = form.cleaned_data['pages']
            com = Command(country, name_vacancy, pages)
            info = com.handle()
            return render(request, 'parserAPP/results.html',
                          context={'info': info, 'vacancy': name_vacancy, 'region': country})
            # return HttpResponseRedirect(reverse('parserAPP:results'))
        else:
            return render(request, 'parserAPP/request.html', context={'form': form})
    else:
        form = Request()
        return render(request, 'parserAPP/request.html', context={'form': form})


def tables(request, id):
    vacancy = get_object_or_404(Vacancies, id=id)
    vacancy = Vacancies.objects.get(id=id)
    keywords = [{'word': str(word)[:str(word).index(':')], 'count': str(word)[str(word).index(':')+1:]} for word in vacancy.words.all()]
    sum_val = 0
    for item in keywords:
        sum_val += int(item['count'])
    for item in keywords:
        item['per'] = round(int(item['count']) / sum_val * 100, 2)
    return render(request, 'parserAPP/tables.html', context={'vacancy': vacancy, 'keywords': keywords})


def results(request):
    return render(request, 'parserAPP/results.html',)

