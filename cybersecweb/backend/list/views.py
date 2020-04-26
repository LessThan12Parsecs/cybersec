from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import JsonResponse
import boto3
session = boto3.Session(profile_name='sec') #profile_name='sec'

def lambdas(request):
    lmda = session.client('lambda')
    response = lmda.list_functions()
    return JsonResponse(response)

def iam_users(request):
    iam = session.client('iam')
    response = iam.list_users()
    for iamuser in response['Users']:
        policies = iam.list_attached_user_policies(UserName=iamuser['UserName'])
        iamuser['Policies'] = policies
    return JsonResponse(response) 

def iam_groups(request):
    iam = session.client('iam')
    response = iam.list_groups()
    return JsonResponse(response)

def iam_roles(request):
    iam = session.client('iam')
    response = iam.list_roles()
    return JsonResponse(response)

def policies(request):
    iam = session.client('iam')
    response = iam.list_policies()
    return JsonResponse(response)

def accounts(request):
    org = session.client('organizations')
    response = org.list_accounts()
    return JsonResponse(response)


    #TODO test
def organization_units(request):
    org = session.client('organizations')
    response = org.list_accounts()
    return JsonResponse(response)

    


