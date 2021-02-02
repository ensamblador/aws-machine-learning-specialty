import os
import io
import boto3
import json
import csv
import pandas as pd

ENDPOINT_NAME = 'xgboost-2021-02-02-18-36-17-798'
runtime= boto3.client('runtime.sagemaker')

# Convert categorical date field
observation_no = "0,54,99,3,999,0,-1.1,94.601,-49.5,0.987,4963.6,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0"
observation_yes = "0,27,139,1,1,1,-1.8,92.89299999999999,-46.2,1.266,5099.1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0"
#observation = observation.replace("-","")

data_no = {"data":observation_no}
actual_no = {"data":"0"}
payload_no = data_no['data']

data_yes = {"data":observation_yes}
actual_yes = {"data":"1"}
payload_yes = data_yes['data']
# print(payload)

response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                    ContentType='text/csv',
                                    Body=payload_no)
# print(response)

result = json.loads(response['Body'].read().decode())
#print('prediction: ', result['predictions'][0]['score'], '\t\tactual: ', str(actual['data']))
print('result: ', result, 'prediction: ', str(actual_no['data']))
