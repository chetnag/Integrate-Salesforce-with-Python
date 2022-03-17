import json
import pandas as pd

from simple_salesforce import Salesforce, SalesforceLogin

loginInfo = json.load(open('login.json'))
username = loginInfo['username']
password = loginInfo['password']
security_token = loginInfo['security_token']
domain = 'login'

session_id, instance = SalesforceLogin(username=username,password=password, security_token=security_token, domain=domain)

sf = Salesforce(instance = instance, session_id = session_id)
print(sf)
values = ['Energy', 'Hospitality']
querySOQL = """SELECT Id, Name, Type, Industry FROM Account WHERE Industry IN('{0}')""".format("','".join(values))
print(querySOQL)

# simple salesforce has 3 methods 
# query(all records archived and unarchived), 
# query_all(no archived records), 
# query_more(no archived records)

recordAccounts = sf.query(querySOQL)
print(recordAccounts)
print(recordAccounts.keys())

# If records exceeding 200 limit > Batch
response = sf.query(querySOQL)
lstRecords = response.get('records')

nextRecordsUrl = response.get('nextRecordsUrl')

while not response.get('done'):
    response = sf.query_more(nextRecordsUrl, identifer_is_url=True)
    lstRecords.extend(response.get('records'))
    nextRecordsUrl = response.get('nextRecordsUrl')

df_records = pd.DataFrame(lstRecords)
print(df_records)

# SOSL 

records = sf.search('FIND {United iOil Installations} RETURNING Opportunity (Id, Name, StageName)')
print(records)

df_recordsSOSL = pd.DataFrame(records.get('searchRecords'))
print(df_recordsSOSL)

