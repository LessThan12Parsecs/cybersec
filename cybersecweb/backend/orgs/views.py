from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import boto3
session = boto3.Session(profile_name='sec2')

def create_account(request, name):
    orgs = session.client('organizations')
    orgs.create_account(
        Email='logs@test.com',
        AccountName=name,
        IamUserAccessToBilling='DENY'
    )
    return HttpResponse("Account " + name + " created")