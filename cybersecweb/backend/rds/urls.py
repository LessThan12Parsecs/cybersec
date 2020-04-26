from django.urls import path
from . import views

urlpatterns = [
    path('list_databases/', views.list_databases, name='rdsdatabases'),
]