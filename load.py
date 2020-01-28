# import dependencies - boto3
import boto3
import csv
import os
import time

files = ['./data/media.csv', './data/project.csv', './data/profile.csv']

table_names = ['dev-csv2ddb-media', 'dev-csv2ddb-project', 'dev-csv2ddb-profile']

# load csv into dictionary
def csv_to_dict(file):
    items = []
    with open(file) as csvfile:
        print("Opening " + file + "...")
        reader = csv.DictReader(csvfile)
        index = next(reader)
        print("Columns: ", index)
        for row in reader:
            data = {}
            for col in index:
                data[col] = row[col]
            
            # data['owner'] = row['owner']
            # data['tags'] = row['tags']
            # data['users'] = row['users']
            # data['projectid'] = row['projectid']
            # data['url'] = row['url']
            items.append(data)

    # Replace empty string values with None type
    for row in items:
        for key, value in row.items():
            if value == '':
                row[key] = None
    
    #print(items)

    return items


def dict_to_dynamodb(items, table_name):
    
    ACCESS_KEY_ID = os.environ['ACCESS_KEY_ID']
    SECRET_ACCESS_KEY = os.environ['SECRET_ACCESS_KEY']
    
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY_ID, 
        aws_secret_access_key=SECRET_ACCESS_KEY
    )
    print("Created session...")

    dynamodb = session.resource('dynamodb')
    db = dynamodb.Table(table_name)
    print("Loading " + table_name + "...")
    print(db.key_schema)

    with db.batch_writer() as batch:
        for item in items:
            print(item)
            batch.put_item(Item=item)
            #print("Item printed:")
            #print(item)

    return print(table_name + " has been loaded.")

if __name__ == '__main__':
    for file, table_name in zip(files, table_names):
        data = csv_to_dict(file)
        dict_to_dynamodb(data, table_name)
        