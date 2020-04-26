from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
import boto3
session = boto3.Session(profile_name=settings.AWS_SETTINGS['credentials'])
# Create your views here.

def ec2_instance(request, id, key, value):
    ec2 = session.client('ec2')
    ec2.create_tags(
        DryRun=False,
        Resources=[
            id, #i-0cee642c57a566e04
        ],
        Tags=[
            {
                'Key':key,
                'Value':value
            },
        ]
    )
    return HttpResponse(" Tagged resource id: " + id + " with key: "+ key + " and value: " + value)

def close_sg_and_tag(request):
     return HttpResponse("Closed ")