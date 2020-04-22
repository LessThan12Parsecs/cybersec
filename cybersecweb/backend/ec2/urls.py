from django.urls import path
from . import views

urlpatterns = [
    path('insecure_groups/',views.insecure_groups, name='Insecure Groups')
]