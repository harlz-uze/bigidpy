# BigID Global settings
BIGID_INSTANCE  = "https://sandbox.bigiddemo.com"
API_URL: str = '/api/v1/'

# Authentication
REFRESH_URL: str = f'{API_URL}refresh-access-token'
USER_URL: str = f'{API_URL}sessions'

# Data Sources URLS
DATASOUCES: str = f'{API_URL}ds_connections/'
GET_DATASOURCES: str = f'{API_URL}file-download/export'
SUPPORTED_DATASOURCES: str = f'{API_URL}ds-connections-types'
SCANNER_STATUS_ALL: str = f'{API_URL}scanner-status/'
SCANNER_JOBS: str = f'{API_URL}scanner_jobs/'