from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from cybersecweb.utils import store
import boto3
session = boto3.Session(profile_name=settings.AWS_SETTINGS['credentials'])


def encrypt_all(request):
    s3 = session.client('s3')
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        s3.put_bucket_encryption(
            Bucket=bucket['Name'],
            ServerSideEncryptionConfiguration={
                'Rules': [
                    {
                        'ApplyServerSideEncryptionByDefault': {
                            'SSEAlgorithm': 'AES256',
                        }
                    },
                ]
            }
    )
    return HttpResponse("All S3 Buckets encryptation activated")


# TODO Check region constraints
def create_bucket(request,bucketName):
    s3 = session.client('s3')
    response = s3.create_bucket(
        ACL='private',
        Bucket=bucketName,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1'
        },
    )
    s3.put_public_access_block(
        Bucket=bucketName,
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        }
    )
    s3.put_bucket_encryption(
        Bucket=bucketName,
        ServerSideEncryptionConfiguration={
            'Rules': [
                {
                    'ApplyServerSideEncryptionByDefault': {
                        'SSEAlgorithm': 'AES256',
                    }
                },
            ]
        }
    )
    return JsonResponse(response)

# Set public access block to account 
def set_pab_to_account(request,accountId):
    s3 = session.client('s3')
    s3.put_public_access_block(
        PublicAccessBlockConfiguration={
            'BlockPublicAcls': True,
            'IgnorePublicAcls': True,
            'BlockPublicPolicy': True,
            'RestrictPublicBuckets': True
        },
        AccountId=accountId
    )
    return HttpResponse("Account id" + accountId + " Has blocked public access to new S3 Buckets")


def list_buckets(request):
    s3 = session.client('s3')
    response = s3.list_buckets()
    for bucket in response['Buckets']: # YOU CAN GET A LOT OF THINGS FROM BUCKETS
        bucketRegion = s3.get_bucket_location(
            Bucket=bucket['Name']
        )
        bucket['Region'] = bucketRegion

        # bucketPolicy = s3.get_bucket_policy(
        #     Bucket=bucket['Name']
        # )
        # bucket['Policy'] = bucketPolicy

        bucketEncryption = s3.get_bucket_encryption(
            Bucket=bucket['Name']
        )
        bucket['Encryption'] = bucketEncryption
    store(response,'S3BUCKETS')
    return JsonResponse(response)

def list__unencrypted_buckets(request):
    s3 = session.client('s3')
    response = s3.list_buckets()
    unencryptedBuckets = 
    for bucket in response['Buckets']: # YOU CAN GET A LOT OF THINGS FROM BUCKETS
        bucketEncryption = s3.get_bucket_encryption(
            Bucket=bucket['Name']
        )
        bucket['Encryption'] = bucketEncryption

    store(response,'S3BUCKETS')
    return JsonResponse(response)
