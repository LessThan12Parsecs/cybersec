# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import JsonResponse
from django.conf import settings
import boto3
session = boto3.Session(profile_name=settings.AWS_SETTINGS['credentials'])

def list_lambdas(request):
    lmda = session.client('lambda')
    response = lmda.list_functions()
    return JsonResponse(response)
