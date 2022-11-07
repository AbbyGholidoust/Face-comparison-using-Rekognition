#!/usr/bin/env python
# coding: utf-8

# # A Simple Face Comparison Code with [AWS Rekognition](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/rekognition.html#Rekognition.Client.compare_faces)

# ## Import Libraries

# In[20]:


import boto3
from pprint import pprint

client = boto3.client('rekognition')


# ## Target Image

# ![Target Image](https://ml-lab1-s3.s3.us-west-2.amazonaws.com/target.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLWVhc3QtMSJHMEUCIC4WlsDBiP30ZEGlnk%2FXGwywYecyHEscHqVXGMTnj%2BHrAiEA%2BATmjNgqlERkJFIz0zDIdDI8nbO57hWycZKxcDlyV8kq5AIIIBAAGgw4MTM5MDU1MTQwNDciDDJm3pmYUm9absv4HCrBAvkSaEYLw4LQzhiTSpwF07ygSzxvHRsTrCFg9yUFQ21pSFQuMWme%2FfgztksT40JV2NCUdiuA8UvgQ%2F2ZK42NL0vOM2EXrGwZDFAllGUOJPC290C5x7aO0EcIUiBBpxigtmCadcPQpNYJvkuNyi0Rm%2BmYsriUOb3AuyjW1OKcAKrsCm5v3y1YbNQGNpb4%2FudcHjRhNQ2cHLkOtKKZDag7HcVI7XTYcFS7hUtF1DxzrUycLD1j8N0x17188UNE9Q%2BQ3N%2BGTiN3nnywybB10rizZuoQoFsYBKWY5MPaeVPiv9O4XfIIigie3RcE5uVNkvi8kVACZcIZBBPQ0fDwwD0kX20tSSzuTIgSqlvJS2oAsWfN03g9hQ0nTmJxrH8x1xynF1xQZSdsBH%2B7%2BDOem5YRvNHRCBE1m%2F7wDaGguyBXgTjXVjDk5aCbBjqzAl6QcBVWxCK73Fu7ZY%2FLJByVEjgKEOnO64dQDk6mymOPDImPoRn6Fu2vPgisrSECKGkYJ6QGoQZ0T4kDwsBKc2c%2F8Hboi82wKS3WpQ%2BleNKAqlSFY4xvzG%2BuuzSSCS4VECFC5jhEhZvbFCpq1IiQ%2BowPDYxuDGYkWKvud6S7XhCGS6kWoUuDhh7tAj4QhZFnrXpWSNGNoyjJvQXXPh4xHuKB7SqYr81hzLd5mwHV%2FrvD0jQUS5zBFB5WH7mTxoTzfeYuNze8CpvG6elCH0tGeBxIQPXgwuSX8T8E4zNpWLdOFpU6F4gBjO1wMTjv60iRPa9dTNJ%2BEW%2FGpWFWWOx15ePhzTh%2FIb6Ixdsa2htYu8Pp%2BZtzmMxbWqOSie38fAw2jwIlhL7AberW1piMvYFVU0J2Q%2Bc%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221107T024758Z&X-Amz-SignedHeaders=host&X-Amz-Expires=1800&X-Amz-Credential=ASIA33AEMRY735XC52B3%2F20221107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=a0b58824c452c4b05ff18eaf3bf18c8b51d7862a9fb592b8f1f3ab0125515f8c)

# ## Source Image

# ![Source Image](https://ml-lab1-s3.s3.us-west-2.amazonaws.com/source.jpg?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLWVhc3QtMSJHMEUCIC4WlsDBiP30ZEGlnk%2FXGwywYecyHEscHqVXGMTnj%2BHrAiEA%2BATmjNgqlERkJFIz0zDIdDI8nbO57hWycZKxcDlyV8kq5AIIIBAAGgw4MTM5MDU1MTQwNDciDDJm3pmYUm9absv4HCrBAvkSaEYLw4LQzhiTSpwF07ygSzxvHRsTrCFg9yUFQ21pSFQuMWme%2FfgztksT40JV2NCUdiuA8UvgQ%2F2ZK42NL0vOM2EXrGwZDFAllGUOJPC290C5x7aO0EcIUiBBpxigtmCadcPQpNYJvkuNyi0Rm%2BmYsriUOb3AuyjW1OKcAKrsCm5v3y1YbNQGNpb4%2FudcHjRhNQ2cHLkOtKKZDag7HcVI7XTYcFS7hUtF1DxzrUycLD1j8N0x17188UNE9Q%2BQ3N%2BGTiN3nnywybB10rizZuoQoFsYBKWY5MPaeVPiv9O4XfIIigie3RcE5uVNkvi8kVACZcIZBBPQ0fDwwD0kX20tSSzuTIgSqlvJS2oAsWfN03g9hQ0nTmJxrH8x1xynF1xQZSdsBH%2B7%2BDOem5YRvNHRCBE1m%2F7wDaGguyBXgTjXVjDk5aCbBjqzAl6QcBVWxCK73Fu7ZY%2FLJByVEjgKEOnO64dQDk6mymOPDImPoRn6Fu2vPgisrSECKGkYJ6QGoQZ0T4kDwsBKc2c%2F8Hboi82wKS3WpQ%2BleNKAqlSFY4xvzG%2BuuzSSCS4VECFC5jhEhZvbFCpq1IiQ%2BowPDYxuDGYkWKvud6S7XhCGS6kWoUuDhh7tAj4QhZFnrXpWSNGNoyjJvQXXPh4xHuKB7SqYr81hzLd5mwHV%2FrvD0jQUS5zBFB5WH7mTxoTzfeYuNze8CpvG6elCH0tGeBxIQPXgwuSX8T8E4zNpWLdOFpU6F4gBjO1wMTjv60iRPa9dTNJ%2BEW%2FGpWFWWOx15ePhzTh%2FIb6Ixdsa2htYu8Pp%2BZtzmMxbWqOSie38fAw2jwIlhL7AberW1piMvYFVU0J2Q%2Bc%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221107T024645Z&X-Amz-SignedHeaders=host&X-Amz-Expires=1800&X-Amz-Credential=ASIA33AEMRY735XC52B3%2F20221107%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=348d3805d437adf135eed4391a394bf98841beb1c571e9e729a52b188bd5fbbc)

# ## Result

# In[21]:


response = client.compare_faces(
    SimilarityThreshold=90,
    SourceImage={
        'S3Object': {
            'Bucket': 'ml-lab1-s3',
            'Name': 'source.jpg',
        },
    },
    TargetImage={
        'S3Object': {
            'Bucket': 'ml-lab1-s3',
            'Name': 'target.jpg',
        },
    },
)


pprint(response)


# In[ ]:




