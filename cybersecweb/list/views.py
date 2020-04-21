from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import JsonResponse
import boto3
session = boto3.Session()

#TODO tag resource

def ec2instances(request):
    ec2 = session.client('ec2')
    response = ec2.describe_instances() #TODO EBS
    return JsonResponse(response)

def s3buckets(request):
    s3 = session.client('s3')
    response = s3.list_buckets() #TODO bucket regions
    return JsonResponse(response)

def rdsdatabases(request):
    rds = session.client('rds')
    response = rds.describe_db_instances()
    return JsonResponse(response)

def vpcs(request):
    ec2 = session.client('ec2')
    response = ec2.describe_vpcs()
    return JsonResponse(response)

def securitygroups(request):
    ec2 = session.client('ec2')
    response = ec2.describe_security_groups()
    return JsonResponse(response)

def lambdas(request):
    lmda = session.client('lambda')
    response = lmda.list_functions()
    return JsonResponse(response)

def iamusers(request):
    iam = session.client('iam')
    response = iam.list_users()
    return JsonResponse(response) #TODO list policies for users

def iamgroups(request):
    iam = session.client('iam')
    response = iam.list_groups()
    return JsonResponse(response)

def iamroles(request):
    iam = session.client('iam')
    response = iam.list_roles()
    return JsonResponse(response)

def policies(request):
    iam = session.client('iam')
    response = iam.list_policies()
    return JsonResponse(response)

