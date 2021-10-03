import boto3
# Get the service resource.
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('artists')


#Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='artists',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    })

#Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='artists')
print('table created with success')