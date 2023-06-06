# Used to deploy DSPM policies to a instance of BigID
import sys
sys.path.append('..')
from bigid import BigID
import csv
import os
from data_types import BigIdPolicy
from policy_engine import dump_policies, delete_policy, write_policy
import json

URL = "https://52.90.10.10:30443"
TEST_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJiaGFybGV5QGJpZ2lkLmNvbSIsImlzQWRtaW4iOmZhbHNlLCJyb2xlSWRzIjpbIjViNjlhNzg4Y2EzYzllMDAxMDFkYWY4YiIsIjViNjlhNzg4Y2EzYzllMDAxMDFkYWY4ZSJdLCJyb2xlcyI6W10sInR5cGUiOiJyZWZyZXNoLXRva2VuIiwidG9rZW5OYW1lIjoiNzIyOGY4Y2UtM2QzMS00NDc5LWE4YzMtYTliOGUxZWE5MmRhIiwidGVuYW50SWQiOiJTSU5HTEVfVEVOQU5UIiwidXVpZCI6bnVsbCwiaWF0IjoxNjg2MDExMzY2LCJleHAiOjE2ODg2MDMzNjZ9.LIhFxOKUq1kLsHs82aEHgZUzlL7XFJ1KSqRHlZMT1YI"


# Get all the polices so we can remove them
#connect to big id
bigid: BigID = BigID(host=URL, port=443, refresh_token=TEST_TOKEN)
bigid.request_refresh_token()


def read_in_csv_from_dump():
    # Delete all the policies from bigId
    for i in os.listdir(os.getcwd()):
        if i.endswith('csv'):
            file_name = i
            filename = open(os.path.join(os.getcwd(), file_name), 'r')
    
    # creating dictreader object
    file = csv.DictReader(filename)
    
    # creating empty lists
    ids = []
    for col in file:
        # month.append(col['month_number'])
        ids.append(col['id'])
        # totalunit.append(col['total_units'])
    print('Total ids deleted:', len(ids))
    for i in ids:
        delete_policy(bigid=bigid, bigid_policy_id=i)

# def read_in_json():
    # ''' Read in the json dump of policies and save them in BigID '''
#    for i in os.listdir(os.getcwd()):
#         if i.endswith('json'):
#             file_name = i
#             filename = open(os.path.join(os.getcwd(), file_name), 'r')

def upload_from_csv():
    ''' Read in all the policies related to dspm and apply them to bigid'''
    # filename = open(os.path.join(os.getcwd(), 'dspm.json'), 'r')
    for i in os.listdir(os.getcwd()):
        if i.endswith('csv'):
            # file_name = i
            filename = open(os.path.join(os.getcwd(), i), 'r')
    file = csv.DictReader(filename)
    # data = filename.readlines()
    # file = csv.DictReader(filename)
    # filename.readlines()
            # data = filename.readlines()
            # print(json.load(filename))
    for i in file:
        # print(json.loads(json.dumps(i)))
        # print(json.dumps(i))
        
        # policy = BigIdPolicy.from_json(i)
        print(i['name'])
        # print(i)
        # write_policy(bigid=bigid, bigid_policy=policy)
        # print(policy)
    # print(data)
    # print(len(data))
# read_in_csv_from_dump()
# create_dspm_policies()
# dump_policies(bigid=bigid, dump_type='json')

def upload_from_json():
    ''' Upload policy objects from json'''
    for i in os.listdir(os.getcwd()):
        if i.endswith('json'):
            # file_name = i
            with open(os.path.join(os.getcwd(), i), 'r') as fo:
                policies = (json.load(fo))
    # print(json.loads(filename.read()))
    for i in policies:
        d = BigIdPolicy.from_json(i)
        # write_policy(bigid=bigid, bigid_policy=d)
        print(d.category)
        # delete_policy(bigid=bigid, bigid_policy_id=d.id)
        write_policy(bigid=bigid, bigid_policy=d)
upload_from_json()