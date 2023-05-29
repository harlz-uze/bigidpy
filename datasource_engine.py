import bigid
import requests
from datetime import datetime
from data_types import BigData
import settings

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

def get_datasource(bigid: bigid.BigID) -> BigData:
    ''' Get a list of data sources
    
    Attributes:
        bigid: BigID instance to use for requests
    
    Returns:
        BigData: BigID dataclass
    
    Raises:
        None
    
    '''
    data: BigData = bigid.make_request(api_path=settings.DATASOUCES)
    return data

def dupliate_datasource(bigid: bigid.BigId) -> BigData:
    ''' Duplicate a data source already configured 
    
    Attributes:
        bigid: BigID instance to use for requests
    
    Returns:
        BigData: BigID dataclass
    
    Raises:
        None
    
    '''
    raise NotImplementedError