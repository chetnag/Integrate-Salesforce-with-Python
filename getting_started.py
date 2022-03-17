import json
import pandas as pd

from simple_salesforce import Salesforce, SalesforceLogin, SFType

loginInfo = json.load(open('login.json'))
username = loginInfo['username']
password = loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

# secure way to connect to salesforce org
session_id, instance = SalesforceLogin(username=username,password=password, security_token=security_token, domain=domain)
sf = Salesforce(instance = instance, session_id = session_id)
print(sf)

#get orgs metadata
metadata_org = sf.describe()
print('data type', type(metadata_org))
print('Maximum no. of records you can retrieve' , metadata_org['maxBatchSize'])

# use panda to get result in list format
df_objects =pd.DataFrame(metadata_org['sobjects'])
print(df_objects)

# convert result into CSV file
df_objects.to_csv('org metadata info.csv', index=False)


account = sf.account
account_metadata = account.describe()

# Method to retrieve metadata according to objects we can type object API name
project = SFType('Account', session_id, instance)
project_metadata = project.describe()
sf_project_metadata = pd.DataFrame(account_metadata.get('fields'))
sf_project_metadata.to_csv('Account object metadata.csv', index=False)


