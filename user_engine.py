# User administration interface

import bigid
import data_types
import settings
from exceptions import UserMethodError

def get_users(bigid: bigid.BigID) -> list[dict[str, str]]:
    ''' Get the list of system users from BigID 
    
    Attributes:
        bigid: BigID instance used for requests 
        
    Returns:
        BigData: Response data from BigID
        
    Raises:
        UserMethodError: When an the bigid instance returns anything other than a 200 status code 
    '''
    data: data_types.BigData = bigid.make_request(api_path=settings.USER_API, http_method='get')
    if data.status_code == 200:
        return data.data['data']['users']
    else:
        raise UserMethodError(f'Status code: {data.status_code}')

def add_user(bigid: bigid.BigID, payload: dict[str, str]) ->None:
    ''' Add a user to BigID 
    
    Attributes:
        bigid: BigId instance used for requests
        
    Returns:
        None
    
    Raises:
        UserMethodError: When the user is failed to be added with the server message
        returned
    '''
    # data: data_types.BigData = bigid.make_request(api_path=settings.USER_API, http_method='post')
    raise NotImplementedError