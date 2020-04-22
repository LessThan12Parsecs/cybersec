from django.urls import path
from . import views

urlpatterns = [
    path('create_account/<name>/', views.create_account, name='Create Account in Organization'),
]