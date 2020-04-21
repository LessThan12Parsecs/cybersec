from django.urls import path
from . import views

urlpatterns = [
    path('ec2instances',views.ec2instances, name='ec2instances'),
    path('s3buckets',views.s3buckets, name='s3buckets'),
    path('rdsdatabases',views.rdsdatabases, name='rdsdatabases'),
    path('vpcs',views.vpcs, name='vpcs'),
    path('securitygroups',views.securitygroups, name='securitygroups'),
    path('lambdas',views.lambdas, name='lambdas'),
    path('iamusers',views.iamusers, name='iamusers'),
    path('iamgroups',views.iamgroups, name='iamgroups'),
    path('iamroles',views.iamroles, name='iamroles'),
    path('policies',views.policies, name='policies'),
]