import click
import boto3
import csv

@click.group()
def cli():
    """
    Load CSV files directly into AWS DynamoDB.
    
    Configure awscli for best results.
    """
    pass

@cli.command(name="list")
def list_tables():
    """List DynamoDB tables."""
    dynamodb_client = boto3.client('dynamodb')
    click.echo(dynamodb_client.list_tables()['TableNames'])

@cli.command(name="create")
@click.option("--table-name", required=True, type=click.STRING, help="Name of DynamoDB table")
@click.option("--partition-key", required=True, type=click.STRING, help="Partition key")
@click.option("--partition-key-type", default='S', show_default=True, 
                                    type=click.STRING, help="S or N")
@click.option("--sort-key", type=click.STRING, help="Optional sort key") # make sort key optional
@click.option("--sort-key-type", default='S', show_default=True, type=click.STRING, help="S or N") # make sort key optional
def table(table_name, partition_key, partition_key_type, sort_key, sort_key_type): 
    """Create a DynamoDB table."""

    dynamodb_client = boto3.client('dynamodb')
    existing_tables = dynamodb_client.list_tables()['TableNames']

    if table_name not in existing_tables:

        key_schema = [{'AttributeName': partition_key, 'KeyType': 'HASH'}]
        attribute_defs = [{'AttributeName': partition_key,'AttributeType': partition_key_type}]
        
        # Sort key option
        if sort_key and sort_key_type:
            key_schema.append({'AttributeName': sort_key,'KeyType': 'RANGE'})
            attribute_defs.append({'AttributeName': sort_key,'AttributeType': sort_key_type})
        
        response = dynamodb_client.create_table(
            TableName=table_name,
            KeySchema=key_schema,
            AttributeDefinitions=attribute_defs,
            ProvisionedThroughput={
                'ReadCapacityUnits': 5, # make parameter
                'WriteCapacityUnits': 5 # make parameter
            }
        )
        
        if response['TableDescription']['TableStatus'] == 'CREATING':
            click.echo(f'Created table: "{table_name}"') # Check response
    else:
        click.echo(f'Table "{table_name}" already exists.')


@cli.command()
@click.argument("files", nargs=-1) # type=click.File("rb"), nargs=-1
@click.option("--table-name", required=True, type=click.STRING, help="Name of DynamoDB table")
def load(files, table_name):
    """Load a DynamoDB table."""
    #click.echo(files)

    session = boto3.Session()
    #click.echo("Created session...")
    dynamodb = session.resource('dynamodb')
    ddb_table = dynamodb.Table(table_name)
    
    # Get table metadata
    click.echo(f'Getting attributes for table "{table_name}"...')
    defs = ddb_table.attribute_definitions
    partition_key = defs[0]['AttributeName'] # partition key name
    partition_key_type = defs[0]['AttributeType'] # partition key type

    if len(defs) > 1:
        sort_key = defs[1]['AttributeName'] # sort key name
        sort_key_type = defs[1]['AttributeType'] # sort key type
    else:
        sort_key = None

    def csv_to_dict(filename):
        items = []
        click.echo("Reading file...")
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            index = reader.fieldnames
            #click.echo(f"Columns: {index}")
            for row in reader:
                data = {}
                for col in index:
                    data[col] = row[col]
                    # Check for numeric key types
                    if col == partition_key and partition_key_type == "N":
                        data[col] = int(data[col])
                    if col == sort_key and sort_key_type == "N":
                        data[col] = int(data[col])
                items.append(data)

        # Replace empty string values with None type
        for row in items:
            for key, value in row.items():
                if value == '':
                    row[key] = None

        return items

    def dict_to_dynamodb(items, table_name):

        click.echo(f'Loading "{table_name}"...')

        try:
            with ddb_table.batch_writer() as batch:
                for item in items:
                    batch.put_item(Item=item)
            click.echo(f'"{table_name}" has been loaded.')
        except Exception as e:
            click.echo(f"Error: {e}")

    for filename in files:
        try:
            items = csv_to_dict(filename)
            dict_to_dynamodb(items, table_name)
        except Exception as e:
            click.echo(f"Error: {e}")