from django.urls import path
from . import views


urlpatterns = [
    path('insecure_groups/',views.insecure_groups, name='Insecure Groups'),
    path('list_instances/',views.list_instances, name='ec2instances'),
    path('list_vpcs/', views.list_vpcs, name ='vpcs'),
    path('list_security_groups/', views.list_security_groups, name ='list_security_groups'),
    path('list_settings/', views.list_settings, name ='list_security_groups'),
    path('secure_sg_and_tag/', views.secure_sg_and_tag, name ='security groups ip'),
]