from django.urls import path
from . import views

urlpatterns = [
    path('ec2_instance/<id>/<key>/<value>/',views.ec2_instance, name='ec2instances'),
]