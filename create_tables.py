# import dependencies - boto3
import boto3
import os

table_names = ['dev-csv2ddb-media', 'dev-csv2ddb-project', 'dev-csv2ddb-profile']
primary_keys = ['owner', 'projectid', 'handle']
sort_keys = ['url', 'date', 'User']

def create_ddb_table(table_name, primary_key, sort_key): 

    dynamodb_client = boto3.client('dynamodb')
    existing_tables = dynamodb_client.list_tables()['TableNames']

    if table_name not in existing_tables:
        print("Creating Table: " + table_name + " ...")
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
        print("Done.")
    else:
        print("Table " + table_name + " already exists.")




if __name__ == '__main__':
    for table_name, primary_key, sort_key in zip(table_names, primary_keys, sort_keys):
        #print(table_name)
        create_ddb_table(table_name, primary_key, sort_key)

