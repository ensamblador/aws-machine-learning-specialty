import boto3
import sys
import argparse


parser = argparse.ArgumentParser(
    description='Esto realiza una limpieza de Sagemaker (endpoints, models, endpoint conf, training jobs, etc')

parser.add_argument('profile', default='default', nargs='?', help='Profile a utilizar (default=default)')
parser.add_argument('region', default='us-east-1', nargs='?', help='Region name (default=us-east-1')

args = parser.parse_args()

session = boto3.Session(profile_name=args.profile)


sagemaker_client = session.client('sagemaker', region_name=args.region)




# ENDPOINTS
response = sagemaker_client.list_endpoints()
endpoints = response['Endpoints']

profile = 'default'
region = 'us-east-1'

print('\nSe encontraron', len(endpoints), 'endpoints\n')

for endpoint in endpoints:
    print('Endpoint Name:',endpoint['EndpointName'], 'Endpoint Status:', endpoint['EndpointStatus'], end='... ')
    del_response = sagemaker_client.delete_endpoint(EndpointName=endpoint['EndpointName'])
    print ('Borrado\n')

#ENDPOINT CONFIGS:

response = sagemaker_client.list_endpoint_configs()
ecs = response['EndpointConfigs']
print('\nSe encontraron', len(ecs), 'endpoints configs\n')

for ec in ecs:
    print('Endpoint Config Name:',ec['EndpointConfigName'], end='... ')
    del_response = sagemaker_client.delete_endpoint_config(EndpointConfigName=ec['EndpointConfigName'])
    print ('Borrado\n')


#MODELS

response = sagemaker_client.list_models()
mds = response['Models']
print('\nSe encontraron', len(mds), 'models\n')

for md in mds:
    print('Model Name:',md['ModelName'], end='... ')
    del_response = sagemaker_client.delete_model(ModelName=md['ModelName'])
    print ('Borrado\n')
