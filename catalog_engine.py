# BigID Python Library Base BigID class
__author__ = "Brenton Harley"
__version__ = "1.0.0"
__status__ = "Development"

import bigid
from data_types import BigData
from exceptions import CatalogException

def get_supported_filters(method: str) -> dict:
    ''' Return supported filters for a given method '''
    methods: tuple(dict[str, list]) = ({'get_pii_findings': ['count'], 'supported_filters': True})
    if method in methods:
        return methods
    return {f'{method}':'No filter support for method', 'supported_filters': None}

def get_findings(bigid: bigid.BigID) -> BigData:
    ''' Get findings from the catalog '''
    data = bigid.make_request(api_path='/api/v1/data-catalog/scan-result-fetch-findings', http_method='POST')
    return data

def get_pii_findings(bigid: bigid.BigID, data_source_name: str = None, filter: str = None) -> BigData:
    ''' get pii findings for all sources'''
    if data_source_name and filter is None:
        ''' when a data source is specified us it '''
        data = bigid.make_request(api_path=f'/api/v1/data-catalog/objects-with-pii/{data_source_name}', http_method='GET')
        return data
    data = bigid.make_request(api_path='/api/v1/data-catalog/objects-with-pii', http_method='GET')
    if filter:
        if get_supported_filters(method='get_pii_findings'):
            return len(data['data'])
    return data
    
