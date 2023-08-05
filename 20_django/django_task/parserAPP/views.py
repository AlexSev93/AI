from .models import Vacancies
from .forms import Request
from .management.commands.fill_db import Command
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView


class VacsListView(ListView):
    model = Vacancies
    template_name = 'parserAPP/vacancies_list.html'

    # TODO: кастыль чтобы показывались только вакансии с навыками, потому что в CreateView добавляется две записи:
    #     1. Полная
    #     2. Без навыков
    def get_queryset(self):
        vac = Vacancies.objects.all()
        new_vac = []
        for item in vac:
            words = item.words.all()
            if words:
                new_vac.append(item)
        vac = new_vac
        return vac


class InfoDetailView(DetailView):
    model = Vacancies
    template_name = 'parserAPP/vacancies_detail.html'


class SearchCreateView(CreateView):
    form_class = Request
    template_name = 'parserAPP/vacancies_create.html'
    success_url = reverse_lazy('parserAPP:vac_list')

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.pages = None
        self.country = None
        self.name_vacancy = None

    def form_valid(self, form):
        if form.is_valid():
            self.name_vacancy = form.cleaned_data.get('vacancy')
            self.country = form.cleaned_data.get('regions')
            self.pages = int(form.cleaned_data.get('pages'))
            Command(self.country, self.name_vacancy, self.pages).handle()
        return super().form_valid(form)


class VacancyDeleteView(DeleteView):
    template_name = 'parserAPP/vacancy_delete.html'
    model = Vacancies
    success_url = reverse_lazy('parserAPP:vac_list')
