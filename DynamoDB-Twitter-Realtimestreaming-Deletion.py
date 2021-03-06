#!/usr/bin/env python
# coding: utf-8

# # Streaming Deleting Dynamodb tweets and storing in s3
# 
# 
# ## Using a DynamoDB table to capture specific tweet aspects from Kinesis

# ### This notebook provides the necessary code to create a dynamoDB table, with the twitterID as the partition key (Primary Key).

# Creating the DynamoDB table, with the twitterID as the primary key. 

# In[46]:


## create a table to store twitter hashtags in DynamoDB
import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='twitterDB1',
    KeySchema=[
        {
            'AttributeName': 'id_str',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id_str',
            'AttributeType': 'S'
        }
    ],
    # the pricing isdetermined by Provisioned Throughput, thus it is kept low
    ProvisionedThroughput={
        'ReadCapacityUnits': 100,
        'WriteCapacityUnits': 100
    }
)
table.meta.client.get_waiter('table_exists').wait(TableName='twitterDB1')


# ### Linking the Kinesis stream to DynamoDB, parsing and storing tweets


## Importing the necessary libraries

import time
import json
import decimal

#Connecting to the kinesis stream-need to specify kinesis stream here
kinesis = boto3.client("kinesis")
shard_id = 'shardId-000000000000' #only one shard
shard_it = kinesis.get_shard_iterator(StreamName="twitter_bigdata", ShardId=shard_id, ShardIteratorType="TRIM_HORIZON")["ShardIterator"]

#connecting to the dynamoDB table
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('twitterDB')

#Parsing the tweets and setting a counter

while 1==1:
    out = kinesis.get_records(ShardIterator=shard_it, Limit=100)
    for record in out['Records']:
        if 'entities' in json.loads(record['Data']):
            twitterId = json.loads(record['Data'])['entities']['id_str']
            if twitterId:
                    for ht in twitterId:
                        twitterId = ht['text']
                        checkItemExists = table.get_item(
                           Key={
                                        'id_str':twitterId
                                }
                            )
                    if 'Item' in checkItemExists:
                        response = table.update_item(
                                Key={
                                    'id_str': twitterId 
                            }, 
                            UpdateExpression="set htCount  = htCount + :val",
                            ConditionExpression="attribute_exists(id_str)",
                            ExpressionAttributeValues={
                                ':val': decimal.Decimal(1) 	
                            },
                            ReturnValues="UPDATED_NEW"
                        )
                    else: 
                                        response = table.update_item(
                                                Key={
                                                        'id_str': twitterId
                                                },
                                                UpdateExpression="set htCount = :val",
                                                ExpressionAttributeValues={
                                                        ':val': decimal.Decimal(1)
                                                },
                                                ReturnValues="UPDATED_NEW"
                                        )    
    shard_it = out["NextShardIterator"]
    time.sleep(1.0)


# Deleting Stream record by performing batch delete


scan = table.scan()
with table.batch_writer() as batch:
    for each in scan['Items']:
        batch.delete_item(
            Key={
                'id_str': twitterId
            }
        )

