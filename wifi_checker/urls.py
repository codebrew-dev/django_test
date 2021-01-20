from django.urls import path
from . import views

app_name = 'wifi_checker'

urlpatterns = [
    path('/bulk/', views.bulk_import, name='bulk'),
    path('', views.index, name='index'),
    path('/<str:location>/', views.detail, name='detail'),
]