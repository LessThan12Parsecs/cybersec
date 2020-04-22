from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import boto3
session = boto3.Session(profile_name='sec')

def insecure_groups(request):
    ec2 = session.client('ec2')
    response = ec2.describe_security_groups()
    insecureGroups = [{}]
    for sg in response['SecurityGroups']:
        for ipPerm in sg['IpPermissions']:
            for ipRange in ipPerm['IpRanges']: #TODO Change this triple loop
                if ipRange['CidrIp'] == '0.0.0.0/0' and ipPerm['IpProtocol'] != '-1':
                    insecureGroups.append(
                        {'Security Group':sg['GroupName'],
                        'Port':ipPerm['FromPort']})
                    
                       
    return JsonResponse({'result':insecureGroups})