import requests
import json


loginInfo = json.load(open('login.json'))
USERNAME = loginInfo['username']
PASSWORD = loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

CONSUMER_KEY = 'Insert consumer key here'
CONSUMER_SECRET = 'Insert consumer secret here'
DOMAIN_NAME = 'Insert domain name here'

# to get access token 
json_data = {
    'grant_type':'password',
    'client_id':CONSUMER_KEY,
    'client_secret':CONSUMER_SECRET,
    'username':USERNAME,
    'password':PASSWORD
}
response_access_token = requests.post(DOMAIN_NAME+'/services/oauth2/token',data=json_data)
print(response_access_token.status_code)
print(response_access_token.reason)
print(response_access_token.json())

access_token = ''
if response_access_token.status_code == 200:
    access_token_id = response_access_token.json()['access_token']
    print('Access token created')
    access_token = access_token_id

print('access_token ',access_token)

# example retreive object metadata
headers = {
    'Authorization' : 'Bearer '+access_token
}

response_sObject = requests.get(DOMAIN_NAME + '/services/data/v53.0/sobjects',headers=headers)
print(response_sObject.reason)
print(response_sObject.json())
