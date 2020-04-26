from django.urls import path
from . import views

urlpatterns = [
    path('create_account/<name>/<email>/', views.create_account, name='Create Account in Organization'),
    path('list_accounts/', views.list_accounts, name='List Organization Accounts')
]