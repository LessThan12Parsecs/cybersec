from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import JsonResponse
import boto3
from django.conf import settings

session = boto3.Session(profile_name=settings.AWS_SETTINGS['credentials']) 

def list_users(request):
    iam = session.client('iam')
    response = iam.list_users()
    for iamuser in response['Users']:
        policies = iam.list_attached_user_policies(UserName=iamuser['UserName'])
        iamuser['Policies'] = policies
    return JsonResponse(response) 

def list_groups(request):
    iam = session.client('iam')
    response = iam.list_groups()
    return JsonResponse(response)

def list_roles(request):
    iam = session.client('iam')
    response = iam.list_roles()
    return JsonResponse(response)

def list_policies(request):
    iam = session.client('iam')
    response = iam.list_policies()
    return JsonResponse(response)


