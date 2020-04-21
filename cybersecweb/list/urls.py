from django.urls import path
from . import views

urlpatterns = [
    path('ec2_instances',views.ec2_instances, name='ec2instances'),
    path('s3_buckets',views.s3_buckets, name='s3buckets'),
    path('rds_databases',views.rds_databases, name='rdsdatabases'),
    path('vpcs',views.vpcs, name='vpcs'),
    path('security_groups',views.security_groups, name='securitygroups'),
    path('lambdas',views.lambdas, name='lambdas'),
    path('iam_users',views.iam_users, name='iamusers'),
    path('iam_groups',views.iam_groups, name='iamgroups'),
    path('iam_roles',views.iam_roles, name='iamroles'),
    path('policies',views.policies, name='policies'),
    path('accounts',views.accounts, name='accounts'),
]