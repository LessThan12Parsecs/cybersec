from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.http import JsonResponse
import boto3
session = boto3.Session(profile_name='sec2') #profile_name='sec'


def ec2_instances(request):
    ec2 = session.client('ec2')
    response = ec2.describe_instances()
    return JsonResponse(response)

def s3_buckets(request):
    s3 = session.client('s3')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        bucketRegion = s3.get_bucket_location(
            Bucket=bucket['Name']
        )
        bucket['Region'] = bucketRegion
    return JsonResponse(response)

def rds_databases(request):
    rds = session.client('rds')
    response = rds.describe_db_instances()
    return JsonResponse(response)

def vpcs(request):
    ec2 = session.client('ec2')
    response = ec2.describe_vpcs()
    return JsonResponse(response)

def security_groups(request):
    ec2 = session.client('ec2')
    response = ec2.describe_security_groups()
    return JsonResponse(response)

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


