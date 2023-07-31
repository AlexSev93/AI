from django.shortcuts import render
from .models import Vacancies, Keywords


# Create your views here.
def main_view(request):
    vacancies = Vacancies.objects.all()
    keywords = Keywords.objects.all()

    styles = ['text-white', 'text-primary', 'text-secondary', 'text-success', 'text-info', 'text-warning',
              'text-danger', 'text-light', 'text-dark', 'text-body', 'text-muted', 'text-black-50']

    return render(request, 'parserAPP/index.html',
                  context={'vacancies': vacancies, 'keywords': keywords, 'styles': styles})


def request_vacancy(request):
    return render(request, 'parserAPP/request.html')
