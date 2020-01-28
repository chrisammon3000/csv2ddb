# import dependencies - boto3
import boto3
import os

table_names = ['dev-csv2ddb-media', 'dev-csv2ddb-project', 'dev-csv2ddb-profile']
primary_keys = ['owner', 'projectid', 'handle']
sort_keys = ['url', 'name', 'User']
sort_key_types = ['S', 'S', 'N']

def create_ddb_table(table_name, primary_key, sort_key, sort_key_type): 

    dynamodb_client = boto3.client('dynamodb')
    existing_tables = dynamodb_client.list_tables()['TableNames']

    if table_name not in existing_tables:
        print("Creating Table: " + table_name + " ...")
        print("Primary key: " + primary_key)
        print("Sort key: " + sort_key)

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
                    'AttributeType': sort_key_type
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
    for table_name, primary_key, sort_key, sort_key_type in zip(table_names, primary_keys, sort_keys, sort_key_types):
        #print(table_name)
        create_ddb_table(table_name, primary_key, sort_key, sort_key_type)

