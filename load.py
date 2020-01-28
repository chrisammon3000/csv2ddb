# import dependencies - boto3
import boto3
import csv
import os

# load csv into dictionary
def csv_to_dict(file):
    items = []
    with open(file) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data = {}
            data['owner'] = row['owner']
            data['tags'] = row['tags']
            data['users'] = row['users']
            data['projectid'] = row['projectid']
            data['url'] = row['url']
            items.append(data)

    # Replace empty string values with None type
    for row in items:
        for key, value in row.items():
            if value == '':
                row[key] = None
                print(key, value)

    return items



def dict_to_dynamodb(items, tableName):
    
    ACCESS_KEY_ID = os.environ['ACCESS_KEY_ID']
    SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']
    
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY_ID, 
        aws_secret_access_key=SECRET_ACCESS_KEY
    )
    print("Created session...")

    dynamodb = session.resource('dynamodb')
    db = dynamodb.Table(tableName)
    print("Connected to DynamoDB...")

    with db.batch_writer() as batch:
        for item in items:
            batch.put_item(Item=item)
            print("item printed:")
            print(item)

if __name__ == '__main__':
    data = csv_to_dict('./data/media.csv')
    dict_to_dynamodb(data, 'python-dynamodb-load-media')