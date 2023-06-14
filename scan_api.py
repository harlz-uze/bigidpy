# interace with the BigID scan api interface, to send data to the BigID api and 
# have it presented in the catalog

from bigid import BigID
from data_types import BigData
import settings

def send_data(bigid: BigID, json_string: dict[str, str]) -> None:
    ''' Send a json object to BigID as a string and analyse it with the 
    scan api 
    
    Attributes:
        bigid: Instance of BigID
        json_string: A json encoded string of key value pairs
        
    Raises:
        EncodeError: Where a json string is not parseable
        ConnectionError: Where the BigID instance is not accepting connections
        for the Scan API
    '''
    data: BigID = bigid.make_request(api_path=f'{settings.SCAN_API}', http_method='post')
    if data.status_code != 200:
        print('Oh dear')