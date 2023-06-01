from dataclasses import dataclass
import requests
from typing import Optional
import exceptions
from data_types import BigData
import settings
import json


@dataclass
class BigID:
    ''' Base class for BigID connectivity '''
    host: str
    port: int
    refresh_token: Optional[str] = None
    verify_ssl: bool = False
    is_connected: bool = False
    refresh_url: str = settings.REFRESH_URL
    user_url: str = settings.USER_URL
    session_token: str = Optional[None]
    
    def request_refresh_token(self) -> None:
        ''' Make a request to BigID and get a token 
        which can be used to make requests via the API
        
        Raises:
            ConnectionError: If no connection is found or anything other than
            a http_status code of 200 is observed'''
        headers: dict[str, str] = {'Content-Type': 'application/json', 'Authorization': self.refresh_token}
        url: str = f'{self.host}{self.refresh_url}'
        try:
            r = requests.get(url=url, headers=headers, verify=self.verify_ssl)
            if r.status_code == 200:
                self.session_token = r.json()['systemToken']
                self.is_connected = True
            else:
                raise exceptions.UnexpectedResponse(status_code=r.status_code, message=f'{r.text}, url={url}')
        except requests.ConnectionError as err:
            print(f'Connection Error has occured: {err}')
            raise exceptions.UnexpectedResponse(status_code=r.status_code, message=r.text)

        except KeyError as err:
            print('No system token has be returned to the client from BigID, please \
                  make sure you have a valid refresh token')
            raise err
    
    def authenticate(self, user: str, password: str) -> None:
        ''' Authenticate with BigID using a user and password combination and store
        token for use in make_request
        
        Args:
            user: A user name with access level required to make API calls
            password: Password string for user
            
        Returns:
            None
        
        Raises:
            InsufficientPriv: Where your API permissions are insufficient to produce
            ConnectionError: Where the BigID server connection failed to be established
        '''
        headers: dict[str, str] = {'Content-Type': 'application/json'}
        payload: dict[str, str] = json.dumps({'username': user, 'password': password})
        url: str = f'{self.host}{self.user_url}'
        try:
            r = requests.post(url=url, headers=headers, data=payload, verify=self.verify_ssl)
            if r.status_code == 200:
                self.session_token = r.json()['auth_token']
                self.is_connected = True
            else:
                raise exceptions.ConnectionError(status_code=r.status_code, message=f'{r.text}, host={url}')
        except requests.ConnectionError as err:
            print(f'Connection Error has occured: {err}')
            raise exceptions.UnexpectedResponse(status_code=r.status_code, message=r.text)
        except KeyError as err:
            print('No system token has be returned to the client from BigID, please')
            raise exceptions.UnexpectedResponse(status_code=r.status_code, message=r.text)
    
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
            except exceptions.ConnectionError as err:
                print(f'Connection Error has occured: {err}')
                raise exceptions.UnexpectedResponse(status_code=r.status_code, message=r.text)
                
            except KeyError as err:
                print('No system token has be returned to the client from BigID, please \
                    make sure you have a valid refresh token')
                raise err
        else:
            print('Session token must have been created and stored. Have you requested a refresh token?')
        