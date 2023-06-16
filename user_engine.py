# BigID Python User methods for actions against BigID Users

__author__ = "Brenton Harley"
__version__ = "1.0.0"
__status__ = "Development"


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

def add_user(bigid: bigid.BigID, user: data_types.User) ->None:
    ''' Add a user to BigID 
    
    Attributes:
        bigid: BigId instance used for requests
        user: User instance
        
    Returns:
        None
    
    Raises:
        UserMethodError: When the user is failed to be added with the server message
        returned
    '''
    data: data_types.BigData = bigid.make_request(api_path=settings.USER_WRITE, http_method='post', user=user)
    if data.status_code != 200:
        raise UserMethodError(f'Unable to add new user: status_code={data.status_code}, message={data.data}')


def modify_user(bigid: bigid.BigID, user: data_types.User) ->None:
    ''' Modify an existing user in BigID 
    
    Attributes:
        bigid: BigId instance used for requests
        user: User instance
        
    Returns:
        None
    
    Raises:
        UserMethodError: When the user failed to be modified with the server message
        returned
    '''
    data: data_types.BigData = bigid.make_request(api_path=settings.USER_WRITE, http_method='put', user=user)
    if data.status_code != 200:
        raise UserMethodError(f'Unable to modify user: status_code={data.status_code}, message={data.data}')