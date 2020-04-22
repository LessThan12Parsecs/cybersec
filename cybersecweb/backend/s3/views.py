from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import boto3
session = boto3.Session()


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
