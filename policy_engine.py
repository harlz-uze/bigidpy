import bigid
import requests
from datetime import datetime
from data_types import BigData, BigIdPolicy
from exceptions import PoliciesNotFound, PolicyWriteError
import json
from typing import Optional
import csv

def dump_policies(bigid: bigid.BigID, file_path: Optional[str]=None, http_method='get') ->None:
    ''' Dump the currently configured Policies from BigID 
    
    Attributes:
        bigid: BigID instance to use for requests
        file_path: The destination of where to save files, defaults to the current
        path you are running this program from if not provided 
        
    Returns:
        PoliciesNotFound: When no policies are found on the platform
    
    Raises:
        None
        '''
    file_obj: str = (
        f'policy_dump_{datetime.strftime(datetime.utcnow(), "%H_%M_%S")}.csv'
    )
        
    data: BigData = bigid.make_request(api_path='/api/v1/compliance-rules/', http_method=http_method)
    try:
        if 'Not Found' in data.data['message']:
            raise PoliciesNotFound
    except TypeError:
        pass
    if file_path is None:
        array: list[dict] = data.data
        headers: list[str] = []
        for each_item in array:
            for k, v in each_item.items():
                if k not in headers:
                    headers.append(k)
        with open(file_obj, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            for data in array:
                writer.writerow(data)

def write_policy(bigid: bigid.BigID, bigid_policy: BigIdPolicy) -> None:
    ''' Write a new policy to BigID instance 
    
    Attributes:
        bigid: BigID instance to use for requests
        policy: A json encoded representation of the policy you want to apply
        to BigId
    
    Raises:
        PolicyWriteError: Where a policy is not processed and stored in BigID
        
    '''
    data: BigData = bigid.make_request(api_path='/api/v1/compliance-rules/', http_method='post', bigid_policy=bigid_policy)
    if data.status_code == 200:
        pass
    else:
        raise PolicyWriteError(message=f'Unable to write policy: {data}')