from django.urls import path
from . import views

urlpatterns = [
    path('list_lambdas/',views.list_lambdas, name='lambdas'),
]