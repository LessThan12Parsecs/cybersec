import sys
import boto3

session = boto3.Session()


#EC2 instances and EBS 
def PrintInstances():
    ec2 = session.client('ec2')
    response = ec2.describe_instances()
    print("==== INSTANCES ====")
    for instance in response['Reservations'][0]['Instances']:
        print("InstanceId: " + instance['InstanceId'] + "  ====  In Region: " 
            + instance['Placement']['AvailabilityZone'] 
            + " === With tag: " + instance['Tags'][0]['Value'])
        print("          =====EBS====")
        for ebs in instance['BlockDeviceMappings']:
            print("VolumeId: " + ebs['Ebs']['VolumeId'])
    pass





#S3 Buckets listing
def PrintS3Buckets():
    s3 = session.client('s3')
    response = s3.list_buckets()
    print("==== S3 Buckets ====")
    for bucket in response['Buckets']:
        bucketRegion = s3.get_bucket_location(
            Bucket=bucket['Name']
        )
        print("Bucket Name: " + bucket['Name'] + " === In Region: " 
                + str(bucketRegion['LocationConstraint']))
    pass



#RDS databases
def PrintRDSDatabases():
    rds = session.client('rds')
    response = rds.describe_db_instances()
    print("==== RDS instances ====")
    for rds in response['DBInstances']:
        print("DB instance id: " + rds['DBInstanceIdentifier'])
    pass



#VPCs
def PrintVPCs():
    ec2 = session.client('ec2')
    response = ec2.describe_vpcs()
    print("==== VPC ====")
    for vpc in response['Vpcs']:
        print("VPC instance id: " + vpc['VpcId'])
    pass


#SecurityGroup
def PrintSecurityGroups():
    ec2 = session.client('ec2')
    response = ec2.describe_security_groups()
    print("==== Security Groups ====")
    for sg in response['SecurityGroups']:
        print("Security Group  id: " + sg['GroupId'])
    pass


#Lambdas
def PrintLambdas():
    lmda = session.client('lambda')
    response = lmda.list_functions()
    print("==== Lambdas ====")
    for lmbd in response['Functions']:
        print("Lambda Name: " + lmbd['FunctionName'])
    pass

#Tag Instance 
def TagInstance(instanceId):
    ec2 = session.client('ec2')
    ec2.create_tags(
        DryRun=False,
        Resources=[
            instanceId, #i-0cee642c57a566e04
        ],
        Tags=[
            {
                'Key':'test',
                'Value':'BORRAR'
            },
        ]
    )
def PrintIAMUsers():
   iam = session.client('iam')
   response = iam.list_users()
   print("==== Users ====")
   for user in response['Users']:
       print("Username: " + user['UserName'])
       policies = iam.list_user_policies(UserName=user['UserName'])
       print("    === With Policies === ")
       for policy in policies['PolicyNames']:
           print(policy)

def PrintIAMGroups():
   iam = session.client('iam')
   response = iam.list_groups()
   print("==== Groups ====")
   for group in response['Groups']:
       print("Group name: " + group['GroupName'])

def PrintIAMRoles():
    iam = session.client('iam')
    response = iam.list_roles()
    print("==== Roles ====")
    for role in response['Roles']:
       print("Role: " + role['RoleName'])

def PrintAllPolicies():
    iam = session.client('iam')
    response = iam.list_policies()
    print("==== Policies ====")
    for p in response['Policies']:
        print("Policy Name:  " + p['PolicyName'])

# PrintIAMUsers() #Problem with credentials  ¿ROLES or permissions?
# PrintIAMGroups()  #Problem with credentials ¿ROLES or permissions?
PrintIAMRoles()
PrintAllPolicies()
 

#Differences between embeded and attached policies?  