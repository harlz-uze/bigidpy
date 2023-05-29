# BigIDpy
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

## Connection Example
``` 
import bigid

bigId = bigid.BigID(host='<mybigid.com>', port=443, refresh_token='<my refresh token>')

bigId.

```