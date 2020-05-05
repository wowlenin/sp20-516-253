#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[60]:


get_ipython().system('pip install TwitterAPI')


# In[75]:


get_ipython().system('pip uninstall twitter -y')


# In[76]:


get_ipython().system('pip install python-twitter')


# In[61]:


#creating the kinesis stream
import boto3

client = boto3.client('kinesis')
response = client.create_stream(
   StreamName='twitter_bigdata', #your streamname here
   ShardCount=1
)


# In[7]:


#importing the necessary packages
from TwitterAPI import TwitterAPI
import json
import boto3
import twitter
#import twitterCreds


#accessing the API
#api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

kinesis = boto3.client('kinesis')

api = twitter.Api(consumer_key, consumer_secret, access_token_key, access_token_secret)

#r = api.request()

#for locations
#r = api.request('statuses/filter', {'locations':'-90,-90,90,90'})
#for userids @abcdef:
#r = api.request('statuses/filter', {'follow':'123456'})
#for general text searches
#r = api.request('statuses/filter', {'track':'iphone'})
#r = api.request('user', {'screen_name':'realDonaldTrump'})

r = api.GetUserTimeline(screen_name="akras14", count=10)



for item in r:
    tweets = [item.AsDict()]
    print (tweets)
    response = kinesis.put_record(StreamName="twitter_bigdata", Data=json.dumps(tweets), PartitionKey="filler")


# In[6]:


import boto3
import time
import json
## aws creds are stored in ~/.boto
kinesis = boto3.client("kinesis")
shard_id = "shardId-000000000000" #only one shard!
pre_shard_it = kinesis.get_shard_iterator(StreamName="twitter_bigdata", ShardId=shard_id, ShardIteratorType="TRIM_HORIZON")
shard_it = pre_shard_it["ShardIterator"]
while 1==1:
     out = kinesis.get_records(ShardIterator=shard_it, Limit=1)
     shard_it = out["NextShardIterator"]
     print(out);
     time.sleep(1.0)


# In[ ]:




