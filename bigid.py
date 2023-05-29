from dataclasses import dataclass
import requests
from typing import Optional
import exceptions
from data_types import BigData


@dataclass
class BigID:
    ''' Base class for BigID connectivity '''
    host: str
    port: int
    refresh_token: str
    verify_ssl: bool = False
    is_connected: bool = False
    refresh_url: str = '/api/v1/refresh-access-token'
    session_token: str = Optional[None]
    
    def request_refresh_token(self) -> None:
        ''' Make a request to BigID and get a token 
        which can be used to make requests via the API
        
        Raises:
            ConnectionError: If no connection is found or anything other than
            a http_status code of 200 is observed'''
        headers: dict[str, str] = {'Content-Type': 'application/json'}
        url: str = f'{self.host}{self.refresh_url}'
        try:
            r = requests.get(url=url, headers=headers, verify=self.verify_ssl)
            if r.status_code == 200:
                self.session_token = r.json()['systemToken']
                self.is_connected = True
            else:
                raise exceptions.ConnectionError(status_code=r.status_code, message='Unable to connect')
        except requests.ConnectionError as err:
            print(f'Connection Error has occured: {err}')
            raise err
        except KeyError as err:
            print('No system token has be returned to the client from BigID, please \
                  make sure you have a valid refresh token')
            raise err
    
    def make_request(self, api_path: str, request: str=None) -> BigData:
        ''' Make a request to BigID instance and return a data 
        
        Args:
            request: Request to be made to the api as json string
            api_path: The API path to make a reques /api/v1/blah
        
        Returns:
            BigData: The BigID data object
            
        Raises:
            InvalidPath: Where a /api/v1/blah doesn't exist
            InsufficientPriv: Where your API permissions are insufficient to produce
            the request being made
            JsonError: Where your json request is incorrectly formatted
            ConnectionError: Where the BigID server connection failed to be established
        '''
        headers: dict[str, str] = {'Content-Type': 'application/json',
                                   'Authorization': self.session_token}
        url: str = f'{self.host}{api_path}'
        if self.session_token is not None:
            try:
                print('Attempting to connect to: {url}')
                r = requests.get(url=url, headers=headers, verify=self.verify_ssl)
                data: BigData = BigData(status_code=200, data=r.json())
                return data
            except requests.ConnectionError as err:
                print(f'Connection Error has occured: {err}')
                raise err
                
            except KeyError as err:
                print('No system token has be returned to the client from BigID, please \
                    make sure you have a valid refresh token')
                raise err
        else:
            print('Session token must have been created and stored. Have you requested a refresh token?')
        