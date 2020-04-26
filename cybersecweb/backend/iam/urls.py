from django.urls import path
from . import views

urlpatterns = [
    path('list_users/',views.list_users, name='iamusers'),
    path('list_groups/',views.list_groups, name='iamgroups'),
    path('list_roles/',views.list_roles, name='iamroles'),
    path('list_policies/',views.list_policies, name='policies'),
]