from parserAPP import views
from django.urls import path



app_name = 'parserAPP'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('request/', views.request_vacancy, name='form'),
    path('tables/<int:id>', views.tables, name='tables'),
    path('results/', views.results, name='results')
]


