# BigIDpy

PLEASE NOTE THIS LIBRARY IS UNDER DEVELOPMENT


The BigID py library is intended to be used as the go to interface with your BigID instance regardless of where it is deployed (on-prem, cloud, or both)

## Pre-requisites - Cloud & On-prem
You need sufficient API permissions and a Token created from the "Access Management" console in the BigID UI

## Authentication
There are 2 types of authentication available to consumers of the BigID API. 1. User/Password & 2. Reresh Token. For BigID cloud customers, please note only Reresh tokens can be used to make API requests

## Classess
- BigID
-- The main connection class uses for establishing a connection to BigID instances and ongoing communcations channels
- BigData -- Used as a data store object where data is returned to the clients

## BigID Class Methods
``` request_refresh_token() ``` used to get a session token using and API token provided via Access Management in the BigID UI
``` make_request() ``` used to make requests against a BigID instance requires a session token to have been created with request_refresh_token first.
``` authenticate() ``` used to authenticate against your BigID instance using a user name and password, not supported by BigID cloud

## Settings
Settings are configured via the settings.py file. These settings are used throughout the code to methods & classes. At a minimum you need the following set for your own environment
```
BIGID_INSTANCE  = "<https://my_big_id_instance>"
API_URL: str = '/api/v1/'
```

## Authenticating
### Refresh Token Example
``` 
import bigid
import policy_engine

# instantiate a bigid instance
bigId = bigid.BigID(host='<mybigid.com>', port=443, refresh_token='<my refresh token>')

# request and access token using your refresh token
bigId.request_refresh_token()


```

### User Name and Password Example
``` 
import bigid
import policy_engine

# instantiate a bigid instance
bigId = bigid.BigID(host='<mybigid.com>', port=443, refresh_token='<my refresh token>')

# request and access token using your user name and password
bigId.authenticate(user='<user name>', password='<password>')

```

### Dumping Policies

```
import bigid
import policy_engine

# instantiate a bigid instance
bigId = bigid.BigID(host='<mybigid.com>', port=443, refresh_token='<my refresh token>')

# request and access token using your refresh token
bigId.authenticate(user='<user name>', password='<password>')

# dump the policies configure in BigID
policy_engine.dump_policies(bigid=bigId)



```

### Adding a Policy

```
import bigid
import policy_engine
from data_types import BigIdPolicy

# instantiate a bigid instance
bigId = bigid.BigID(host='<mybigid.com>', port=443, refresh_token='<my refresh token>')

# request and access token using your refresh token
bigId.authenticate(user='<user name>', password='<password>')

# define a policy object you want to save
bigid_policy=BigIdPolicy(actions=[], complianceRuleCalc={'bigidQuery':    'field="classifier.Australian Bank Account Number near Term ID"', 'maxFindings': '1000'},
    description='Some description for my policy', is_enabled=True, name='The name of my policy',
    owner='owner@email', type='catalog', apps=[], 
    taskSettings={'includeLinkToInventory': True, 'includeObjectsReport': False},
    category='GDPR')


# Create a policy to save the policies configure in BigID
policy_engine.write_policy(bigid=bigId, bigid_policy=bigid_policy)



```