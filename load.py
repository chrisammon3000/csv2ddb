import boto3
import csv
import os
import time

# File paths of csvs from Google sheets
files = ['./data/media.csv', './data/profile.csv', './data/project.csv']

# Order table names in same order as filepaths
table_names = ['dev-csv2ddb-media', 'dev-csv2ddb-profile', 'dev-csv2ddb-project']

# load csv into dictionary
def csv_to_dict(file):
    items = []
    with open(file) as csvfile:
        print("Opening " + file + "...")
        reader = csv.DictReader(csvfile)
        index = reader.fieldnames
        print("Columns: ", index)
        for row in reader:
            data = {}
            
            # Change User to integer type
            for col in index:
                data[col] = row[col]
                if col == 'User':
                    data[col] = int(data[col])
        
            items.append(data)

    # Replace empty string values with None type
    for row in items:
        for key, value in row.items():
            if value == '':
                row[key] = None

    return items


def dict_to_dynamodb(items, table_name):
    
    session = boto3.Session()
    print("Created session...")

    dynamodb = session.resource('dynamodb')
    db = dynamodb.Table(table_name)
    print("Loading " + table_name + "...")
    print(db.key_schema)

    with db.batch_writer() as batch:
        for item in items:
            print(item)
            batch.put_item(Item=item)

    return print(table_name + " has been loaded.")

if __name__ == '__main__':
    for file, table_name in zip(files, table_names):
        data = csv_to_dict(file)
        dict_to_dynamodb(data, table_name)
        