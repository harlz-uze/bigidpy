# The scanner engine is designed to provide the easiet access to scanner
# details and statistics programatically

__author__ = "Brenton Harley"
__version__ = "1.0.0"
__status__ = "Development"

import bigid
from data_types import BigData
import settings

def get_scanner_status_all(bigid: bigid.BigID) -> BigData:
    ''' Get status of all scanners from the BigID instance 
    
    Attributes:
        bigid: BigID instance to use for requests

    Returns:
        BigData: BigID dataclass
    
    Raises:
        None 
    '''
    data: BigData = bigid.make_request(api_path=settings.SCANNER_STATUS_ALL, http_method='get')
    return data

def get_scanner_by_id(bigid: bigid.BigID, scanner_id: int) -> BigData:
    ''' Get status of a scanner using the scanner ID
    
    Attributes:
        bigid: BigID instance to use for requests

    Returns:
        BigData: BigID dataclass
    
    Raises:
        None 
    '''
    data: BigData = bigid.make_request(api_path=f'{settings.SCANNER_STATUS_ALL}%7B{scanner_id}%7', http_method='get')
    return data

def get_scanner_jobs(bigid: bigid.BigID) -> BigData:
    ''' Get the count and pending jobs from scanners
    
    Attributes:
        bigid: BigID instance to use for requests

    Returns:
        BigData: BigID dataclass
    
    Raises:
        None 
    '''
    data: BigData = bigid.make_request(api_path=f'{settings.SCANNER_JOBS}', http_method='get')
    return data
    