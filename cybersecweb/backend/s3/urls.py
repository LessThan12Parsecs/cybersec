from django.urls import path
from . import views

urlpatterns = [
    path('encrypt_all/',views.encrypt_all, name='Encrypt All'),
    path('create_bucket/<bucketName>/',views.create_bucket, name='Create Bucket'),
    path('list_buckets/',views.list_buckets, name='s3buckets'),
]