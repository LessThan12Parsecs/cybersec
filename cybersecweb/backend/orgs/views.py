from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
import boto3
session = boto3.Session(profile_name=settings.AWS_SETTINGS['credentials'])

def create_account(request, name, email):
    orgs = session.client('organizations')
    orgs.create_account(
        Email=email,
        AccountName=name,
        IamUserAccessToBilling='DENY'
    )
    return HttpResponse("Account " + name + " created")

def list_accounts(request):
    org = session.client('organizations')
    response = org.list_accounts()
    return JsonResponse(response)


    #TODO test
def organization_units(request):
    org = session.client('organizations')
    response = org.list_accounts()
    return JsonResponse(response)

    