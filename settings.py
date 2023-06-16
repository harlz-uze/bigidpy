# BigID Python Settings for the BigID Python Library 

__author__ = "Brenton Harley"
__version__ = "1.0.0"
__status__ = "Development"

import logging
import os

# BigID Global settings
BIGID_INSTANCE  = "https://<insert_your_big_instance>"
API_URL: str = '/api/v1/'

# Global Logging
FORMAT = '%(asctime)s: %(message)s'
logger = logging.getLogger('Bigidpy')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(os.path.join(os.path.join(os.getcwd(), 'logs'), 'bigidpy.log'))
fh.setFormatter(logging.Formatter(FORMAT))
fh.setLevel(logging.INFO)
logger.addHandler(fh)

# Authentication
REFRESH_URL: str = f'{API_URL}refresh-access-token'
USER_URL: str = f'{API_URL}sessions'

# Data Sources URLS
DATASOUCES: str = f'{API_URL}ds_connections/'
GET_DATASOURCES: str = f'{API_URL}file-download/export'
SUPPORTED_DATASOURCES: str = f'{API_URL}ds-connections-types'
SCANNER_STATUS_ALL: str = f'{API_URL}scanner-status/'
SCANNER_JOBS: str = f'{API_URL}scanner_jobs/'

# Scan API
SCAN_API: str = f'{API_URL}scan-api/analyze'

# Connect App Global settings
CONNECT_API: str = f'{BIGID_INSTANCE}:8000'

# User administration
USER_API: str = f'{API_URL}system-users'
USER_WRITE: str = f'{API_URL}system_users'