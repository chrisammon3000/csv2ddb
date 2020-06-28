import click
import boto3
import csv

@click.group()
def cli():
    pass

@cli.command()
@click.option("--table-name", required=True, type=click.STRING)
@click.option("--primary-key", required=True, type=click.STRING)
@click.option("--primary-key-type", required=True, default='S', show_default=True, type=click.STRING)
@click.option("--sort-key", required=True, type=click.STRING)
@click.option("--sort-key-type", required=True, type=click.STRING)
def table(table_name, primary_key, primary_key_type, sort_key, sort_key_type): 

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
                    'AttributeType': primary_key_type
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
        click.echo("Created table: " + table_name)
    else:
        click.echo(f"Table {table_name} already exists.")

@cli.command()
@click.argument("files", nargs=-1) # type=click.File("rb"), nargs=-1
@click.option("--table-name", required=True, type=click.STRING)
def load(files, table_name):
    click.echo(files)

    def csv_to_dict(filename):
        items = []
        with open(filename) as csvfile:
            click.echo(f"Opening {filename}")
            reader = csv.DictReader(csvfile)
            index = reader.fieldnames
            click.echo(f"Columns: {index}")
            for row in reader:
                data = {}
                # Change User to integer type
                for col in index:
                    data[col] = row[col]
                    # if col == 'User':
                    #     data[col] = int(data[col])
                items.append(data)

        # Replace empty string values with None type
        for row in items:
            for key, value in row.items():
                if value == '':
                    row[key] = None

        return items

    def dict_to_dynamodb(items, table_name):
        
        session = boto3.Session()
        click.echo("Created session...")

        dynamodb = session.resource('dynamodb')
        db = dynamodb.Table(table_name)
        click.echo((f"Loading {table_name}")
        click.echo((db.key_schema)

        try:
            with db.batch_writer() as batch:
                for item in items:
                    batch.put_item(Item=item)
            click.echo(f"{table_name} has been loaded.")
        except Exception as e:
            click.echo(f"Error: {e}")

    for filename in files:
        try:
            items = csv_to_dict(filename)
            dict_to_dynamodb(items, table_name)
        except Exception as e:
            click.echo(f"Error: {e}")