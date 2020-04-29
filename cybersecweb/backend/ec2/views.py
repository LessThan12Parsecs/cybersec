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
    # store(response,'SECURITY_GROUPS')
    return JsonResponse(response)

def list_settings(request):
    return render(request,'index.html')


def secure_sg_and_tag(request):
    ec2 = session.client('ec2')
    response = ec2.describe_security_groups()
    store(response,'SECURITY_GROUPS')
    insecureGroups = [{}]
    for sg in response['SecurityGroups']:
        for ipPerm in sg['IpPermissions']:
            if ipPerm['IpProtocol'] == '-1':
                insecureGroups.append(
                        {'GroupId':sg['GroupId'],
                        'IpPermissions':ipPerm})
            else:
                # for ipRange in ipPerm['IpRanges']:
                #     if ipRange['CidrIp'] == '0.0.0.0/0':
                insecureGroups.append(
                    {'GroupId':sg['GroupId'],
                    'IpPermissions':ipPerm})
    for isg in insecureGroups:
        if isg.get('GroupId') == None:
            pass
        else:   
            if isg['GroupId'] == 'sg-017812d1c31def71f':
                return JsonResponse({'result': isg})
                # ec2.revoke_security_group_ingress(
                #     GroupId = isg['GroupId'],
                #     IpPermissions = sg['IpPermissions']
                # )        



                # ec2.update_security_group_rule_descriptions_ingress(
                #     GroupId = sg['GroupId'],
                #     IpPermissions = [
                #         {
                #             'FromPort': ipPerm['FromPort'],
                #             'IpProtocol': ipPerm['IpProtocol'],
                #             'IpRanges': [
                #                 {
                #                     'CidrIp': '203.0.113.0/16',
                #                     'Description': 'Acesso por SSH desde la oficina',
                #                 },
                #             ],
                #             'ToPort': ipPerm['FromPort'],
                #         },
                #     ]
                # )
                        # tag_resource(sg['GroupId'],'IpRange','Limited')

    # ec2.revoke_security_group_ingress()(
    #                 GroupId = 'sg-017812d1c31def71f',
    #                 IpPermissions = [
    #                     {
    #                         'FromPort': 22,
    #                         'IpProtocol': 'tcp',
    #                         'IpRanges': [
    #                             {
    #                                 'CidrIp': '0.0.0.0/0',
    #                             },
    #                         ],
    #                         'ToPort': 22,
    #                     },
    #                 ]
    #             )

    # return JsonResponse({'result':insecureGroups})                
    # return HttpResponse('Updated rules')
