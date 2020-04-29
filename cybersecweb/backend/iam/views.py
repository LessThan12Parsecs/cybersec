from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import JsonResponse
import boto3
from django.conf import settings
from cybersecweb.utils import store
import json

session = boto3.Session(profile_name=settings.AWS_SETTINGS['credentials']) 

def list_users(request):
    iam = session.client('iam')
    response = iam.list_users()
    for iamuser in response['Users']:
        policies = iam.list_attached_user_policies(UserName=iamuser['UserName'])
        iamuser['Policies'] = policies
        groups = iam.list_groups_for_user(UserName=iamuser['UserName'])
        iamuser['Groups'] = groups
    store(response,'USERS')
    return JsonResponse(response) 

def list_groups(request):
    iam = session.client('iam')
    response = iam.list_groups()
    return JsonResponse(response)

def list_roles(request):
    iam = session.client('iam')
    response = iam.list_roles()
    store(response,'ROLES')
    return JsonResponse(response)

def list_policies(request):
    iam = session.client('iam')
    response = iam.list_policies()
    store(response,'POLICIES')
    return JsonResponse(response)



