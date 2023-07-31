from parserAPP import views
from django.urls import path

urlpatterns = [
    path('', views.main_view),
    path('request/', views.request_vacancy),
]