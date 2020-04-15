import sys
import boto3

session = boto3.Session(profile_name='sec')
ec2 = session.client('ec2')

response = ec2.describe_instances()


# # Tagging a ec2 instance
# ec2.create_tags(
#         DryRun=False,
#         Resources=[
#             'i-0cee642c57a566e04',
#         ],
#         Tags=[
#             {
#                 'Key':'test',
#                 'Value':'BORRAR'
#             },
#         ]
#     )



#Quick test of showing and tagging the InstancesIds and the EBS VolumesIds
print("====INSTANCES====")
for instance in response['Reservations'][0]['Instances']:
    print("InstanceId: " + instance['InstanceId'] + "  ====  In Region: " 
            + instance['Placement']['AvailabilityZone'] 
            + " === With tag: " + instance['Tags'][0]['Value'])
    print("          =====EBS====")
    for ebs in instance['BlockDeviceMappings']:
        print("VolumeId: " + ebs['Ebs']['VolumeId'])



#S3 Buckets listing
s3 = session.client('s3')
response = s3.list_buckets()
print("====S3 Buckets====")
for bucket in response['Buckets']:
    bucketRegion = s3.get_bucket_location(
        Bucket=bucket['Name']
    )
    print("Bucket Name: " + bucket['Name'] + " === In Region: " + str(bucketRegion['LocationConstraint']))



#RDS databases
rds = session.client('rds')
response = rds.describe_db_instances()
print("====RDS instances====")
for rds in response['DBInstances']:
    print("DB instance id: " + rds['DBInstanceIdentifier'])



#VPCs
response = ec2.describe_vpcs()
print("====VPC====")
for vpc in response['Vpcs']:
    print("VPC instance id: " + vpc['VpcId'])


#SecurityGroup
response = ec2.describe_security_groups()
print("====Security Groups====")
for sg in response['SecurityGroups']:
    print("Security Group  id: " + sg['GroupId'])


#Lambdas
lmda = session.client('lambda')
response = lmda.list_functions()
print("====Lambdas====")
for lmbd in response['Functions']:
    print("Lambda Name: " + lmbd['FunctionName'])