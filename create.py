# import dependencies - boto3
import boto3
import os

# create access key and secret variables
# ACCESS_KEY_ID = os.environ['ACCESS_KEY_ID']
# SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']

# print(ACCESS_KEY_ID)
# print(SECRET_ACCESS_KEY)

# session = boto3.session(
#     region_name='us-east-1', 
#     aws_access_key_id=ACCESS_KEY_ID, 
#     aws_secret_access_key=SECRET_ACCESS_KEY
# )

table_names = ['dev-csv2ddb-media', 'dev-csv2ddb-project', 'dev-csv2ddb-profile']
primary_keys = ['owner', 'projectid', 'handle']
sort_keys = ['url', 'date', 'User']

# debug

def create_ddb_table(table_name, primary_key, sort_key): 

    print("Creating Table: " + table_name)

    dynamodb_client = boto3.client('dynamodb')
    existing_tables = dynamodb_client.list_tables()['TableNames']

    if table_name not in existing_tables:
        response = dynamodb_client.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': primary_key,
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': sort_key,
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': primary_key,
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': sort_key,
                    'AttributeType': 'N'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        print(response)

        #table.meta.client.get_waiter('table_exists').wait(TableName=table_name)

        #print(table_name, table.item_count)




# if __name__ == '__main__':
    for table_name, primary_key, sort_key in zip(table_names, primary_keys, sort_keys):
        create_ddb_table(table_name, primary_key, sort_key)

