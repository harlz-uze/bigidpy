import bigid
from datetime import datetime
from data_types import BigData, BigIdPolicy
from exceptions import PoliciesNotFound, PolicyWriteError
import json
from typing import Optional
import csv
import os
from settings import logger 

LOGGER: str = 'PolicyEngine'

def dump_policies(bigid: bigid.BigID, file_path: Optional[str]=None, http_method='get', dump_type: str = 'csv') ->None:
    ''' Dump the currently configured Policies from BigID into CSV
    
    Attributes:
        bigid: BigID instance to use for requests
        file_path: The destination of where to save files, defaults to the current
        path you are running this program from if not provided 
        
    Returns:
        PoliciesNotFound: When no policies are found on the platform
    
    Raises:
        None
        '''
   #  TODO: Use the BigIdPolicy object when dumping policies
    file_obj: str = (
        f'policy_dump_{datetime.strftime(datetime.utcnow(), "%H_%M_%S")}.csv'
    )
    json_file: str = f'policy_dump_{datetime.strftime(datetime.utcnow(), "%H_%M_%S")}.json'
        
    data: BigData = bigid.make_request(api_path='/api/v1/compliance-rules/', http_method=http_method)
    try:
        if 'Not Found' in data.data['message']:
            raise PoliciesNotFound
    except TypeError:
        pass
    if file_path is None and dump_type == 'csv':
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
    if dump_type is 'json':
        ''' Dump policies out as a json encoded dataclass '''
        output_json: list = []
        logger.debug(f'{LOGGER}: Running JSON Policy Dump: object count %s, item:[0] %s', len(data.data), data.data[0])
        for each_policy in data.data:
            try:
                d: BigIdPolicy = BigIdPolicy.from_json(json.dumps(each_policy))
                logger.debug('%s, %s', LOGGER, d.to_json())
                output_json.append(d.to_json())
            except KeyError as err:
                if err == 'apps':
                    d: BigIdPolicy = BigIdPolicy(actions=each_policy['actions'], apps=[], complianceRuleCalc=each_policy['complianceRuleCalc'],
                        description=each_policy['description'], is_enabled=each_policy['is_enabled'],
                        name=each_policy['name'], owner=each_policy['owner'], taskSettings=each_policy['taskSettings'],
                        type=each_policy['type'], id=each_policy['id'], category=each_policy['category'])
                    output_json.append(d.to_json())
                elif err == 'category':
                    d: BigIdPolicy = BigIdPolicy(actions=each_policy['actions'], apps=each_policy['apps'], complianceRuleCalc=each_policy['complianceRuleCalc'],
                        description=each_policy['description'], is_enabled=each_policy['is_enabled'],
                        name=each_policy['name'], owner=each_policy['owner'], taskSettings=each_policy['taskSettings'],
                        type=each_policy['type'], id=each_policy['id'], category='')
                    output_json.append(d.to_json())
                else:
                    logger.info('Unable to write policy to file: %s', err)
                
        with open(json_file, 'w+') as jsonfile:
            jsonfile.write(json.dumps(output_json))
        
    logger.info('%s: Export Complete: wrote: %s policies to file', LOGGER, len(output_json))

def write_policy(bigid: bigid.BigID, bigid_policy: BigIdPolicy) -> None:
    ''' Write a new policy to BigID instance 
    
    Attributes:
        bigid: BigID instance to use for requests
        policy: A json encoded representation of the policy you want to apply
        to BigId
    
    Raises:
        PolicyWriteError: Where a policy is not processed and stored in BigID
        
    '''
    logger.info('%s: Writing Policies...', LOGGER)
    
    data: BigData = bigid.make_request(api_path='/api/v1/compliance-rules/', http_method='post', bigid_policy=bigid_policy)
    if data.status_code != 200:
        raise PolicyWriteError(message=f'Unable to write policy: {data}')

def delete_policy(bigid: bigid.BigID, bigid_policy_id: str) -> None:
    ''' Delete a single policy by where the policy id an exact match
     Attributes:
        bigid: BigID instance to use for requests
        policy: A json encoded representation of the policy you want to apply
        to BigId
    Raises:
        PolicyWriteError: Where the policy is unable to be removed
    '''
    logger.info('%s: Deleting Policies...', LOGGER)
    data: BigData = bigid.make_request(api_path='/api/v1/compliance-rules/', http_method='delete', bigid_policy_id=bigid_policy_id)
    if data.status_code != 200:
        raise PolicyWriteError(message=f'Unable to write policy: {data}')
    logger.info('%s: Policies deleted', LOGGER)
    