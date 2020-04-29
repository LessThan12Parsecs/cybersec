from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import boto3
from django.conf import settings
from tag.views import tag_resource
from cybersecweb.utils import store

session = boto3.Session(profile_name=settings.AWS_SETTINGS['credentials'])


def list_instances(request): 
    ec2 = session.client('ec2')
    response = ec2.describe_instances()
    return JsonResponse(response)

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

def list_vpcs(request):
    ec2 = session.client('ec2')
    response = ec2.describe_vpcs()
    store(response,'VPCS')
    return JsonResponse(response)

def list_security_groups(request):
    ec2 = session.client('ec2')
    response = ec2.describe_security_groups()
    store(response,'SECURITY_GROUPS')
    return JsonResponse(response)

def list_settings(request):
    return render(request,'index.html')


def secure_sg_and_tag(request):
    ec2 = session.client('ec2')
    response = ec2.describe_security_groups()
    insecureGroups = []
    for sg in response['SecurityGroups']:
        isGroupInsecure = False
        insecurePerms = []
        for ipPerm in sg['IpPermissions']:
            if ipPerm['IpProtocol'] == '-1':
                insecurePerms.append(ipPerm)
                isGroupInsecure = True
            elif ipPerm['IpProtocol'] == 'tcp' or ipPerm['IpProtocol'] == 'udp' or ipPerm['IpProtocol'] == 'icmp' or ipPerm['IpProtocol'] == 'tcicmpv6p':
                for ipRange in ipPerm['IpRanges']:
                    if ipRange['CidrIp'] == '0.0.0.0/0':
                        insecurePerms.append(ipPerm)
                        isGroupInsecure = True
        if isGroupInsecure:
            insecureGroups.append(
                        {'GroupId':sg['GroupId'],
                        'IpPermissions':insecurePerms})
    store(insecureGroups,'SECURITY_GROUPS')
    for isg in insecureGroups:
        # ec2.revoke_security_group_ingress(
        #     GroupId = isg['GroupId'],
        #     IpPermissions = isg['IpPermissions']
        # )
        
        # ec2.authorize_security_group_ingress(
        #     GroupId = insecureGroups[0]['GroupId'],
        #     IpPermissions = insecureGroups[0]['IpPermissions']
        # )
        tag_resource(isg['GroupId'],'vulnerability','OPEN')    
    return HttpResponse('Groups Secured')
    