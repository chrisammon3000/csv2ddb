# import dependencies - boto3
import boto3
import os


# create access key and secret variables
ACCESS_KEY_ID = os.environ['ACCESS_KEY_ID']
SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']

# create dynamodb client
db = boto3.client('dynamodb', 
                    region_name='us-east-1', 
                    aws_access_key_id=ACCESS_KEY_ID, 
                    aws_secret_access_key=SECRET_ACCESS_KEY)

tableName = 'python-dynamodb-load-media-2'

# create table using attributes
# table = db.create_table(
#     TableName=tableName, 
#     KeySchema=[
#         {
#             'AttributeName': 'handle', 
#             'KeyType': 'HASH'
#         },
#         {
#             'AttributeName': 'SiteName',
#             'KeyType': 'RANGE'
#         },
#         {
#             'AttributeName': 'FirstName',
#             'KeyType': 'RANGE'
#         },
#         {
#             'AttributeName': 'LastName',
#             'KeyType': 'RANGE'
#         },
#         {
#             'AttributeName': 'Email',
#             'KeyType': 'RANGE'
#         },
#         {
#             'AttributeName': 'password',
#             'KeyType': 'RANGE'
#         },
#         {
#             'AttributeName': 'experience',
#             'KeyType': 'RANGE'
#         },
#         {
#             'AttributeName': 'interests_tags',
#             'KeyType': 'RANGE'
#         },
#         {
#             'AttributeName': 'following_users',
#             'KeyType': 'RANGE'
#         },
#         {
#             'AttributeName': 'profile_fg',
#             'KeyType': 'RANGE'
#         },
#         {
#             'AttributeName': 'profile_bg',
#             'KeyType': 'RANGE'
#         }
#     ],
#     AttributeDefinitions=[
#         {
#             'AttributeName': 'handle',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'SiteName',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'FirstName',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'LastName',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'Email',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'password',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'experience',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'interests_tags',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'following_users',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'profile_fg',
#             'AttributeType': 'S'
#         },
#         {
#             'AttributeName': 'profile_bg',
#             'AttributeType': 'S'
#         }
#     ],
#     ProvisionedThroughput={
#         'ReadCapacityUnits': 5,
#         'WriteCapacityUnits': 5
#     }
# )

# table.meta.client.get_waiter('table_exists').wait(TableName='users')

# print(table.item_count)