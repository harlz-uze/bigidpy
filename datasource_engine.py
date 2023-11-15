# BigID Python Library Data Source Engine used for actions on Data Sources
__author__ = "Brenton Harley"
__version__ = "1.0.0"
__status__ = "Development"

import bigid
import requests
from datetime import datetime
from data_types import BigData
import settings
from typing import Optional

def add_datasource(bigid: bigid.BigID, ) -> BigData:
    ''' Add a data source to your BigID instance
    
    Attributes:
        bigid: BigID instance to use for requests

    Returns:
        BigData: BigID dataclass
    
    Raises:
        None 
    '''
    raise NotImplementedError

def get_datasource(bigid: bigid.BigID, datasource_name: Optional[str]=None) -> BigData:
    ''' Get a list of data sources
    
    Attributes:
        bigid: BigID instance to use for requests
    
    Returns:
        BigData: BigID dataclass
    
    Raises:
        None
    
    '''
    if datasource_name !=None:
        return bigid.make_request(api_path=settings.DATASOUCES, http_method='get',
                                  datasource=datasource_name)
    data: BigData = bigid.make_request(api_path=settings.DATASOUCES, http_method='get')
    return data

def get_supported_datasources(bigid: bigid.BigID) -> BigData:
    ''' Get a list of the platforms currently supported data sources 
    
    Attributes:
        bigid: BigID instance to use for requests
    
    Returns:
        BigData: BigID dataclass
    
    Raises:
        None
    
    '''
    data: BigData = bigid.make_request(api_path=settings.SUPPORTED_DATASOURCES)
    return data

def duplicate_datasource(bigid: bigid.BigID, data_source: str) -> BigData:
    ''' Duplicate a data source already configured 
    
    Attributes:
        bigid: BigID instance to use for requests
        data_source: The name of the data source to be duplicated
    
    Returns:
        BigData: BigID dataclass
    
    Raises:
        NoSuchDataSource: Where a data source names doesn't exist in the list
        of confgured data sources
    
    '''
    raise NotImplementedError