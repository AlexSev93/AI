from parserAPP import views
from django.urls import path


app_name = 'parserAPP'

urlpatterns = [
    path('', views.VacsListView.as_view(), name='vac_list'),
    path('vacancies-detail/<int:pk>/', views.InfoDetailView.as_view(), name='vac_detail'),
    path('vacancies-create/', views.SearchCreateView.as_view(), name='vac_create'),
    path('vacancy-delete/<int:pk>/', views.VacancyDeleteView.as_view(), name='vac_delete'),
]


