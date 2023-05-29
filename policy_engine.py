import bigid
import requests
from datetime import datetime
from data_types import BigData

def dump_policies(bigid: bigid.BigID, file_path: str=None) ->None:
    ''' Dump the currently configured Policies from BigID 
    
    Attributes:
        bigid: BigID instance to use for requests
        file_path: The destination of where to save files, defaults to the current
        path you are running this program from if not provided 
        
    Returns:
        Nothing
    
    Raises:
        ConnectionError: If the connection fails to be establised
        InsufficientPriv: Where your access is not high enough to make the request and 
        the BigID instance has denied your request
        '''
    file_obj: str = (
        f'policy_dump_{datetime.strftime(datetime.utcnow(), "%H_%M_%S")}.csv'
    )
    try:
        
        data: BigData = bigid.make_request(api_path='/api/v1/compliance-rules')
        if file_path is None:
            with open(file_obj, 'w+') as f:
                f.write(str(data))
    except (requests.ConnectionError) as err:
        print(f'Failed to establish a connection to BigID instance: {bigid.url}')