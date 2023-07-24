# BigID Python Library Exceptions

__author__ = "Brenton Harley"
__version__ = "1.0.0"
__status__ = "Development"

class InvalidPathError(Exception):
    def __init__(
        self, message="Invalid API path error, url incorrectly formatted or doesn't exist"
    ):
        self.message = message
        super().__init__(self.message)


class InsufficientPriv(Exception):
    def __init__(self, status_code, message='API Permissions are insufficient for you to make this request'):
        self.status_code = status_code
        self.message = message
        super().__init__(f'status_code: {status_code}, message: {self.message}')


class JsonError(Exception):
    def __init__(self, message='JSON is not correctly formatted and request not made'):
        self.message = message
        super().__init__(f'message: {self.message}')


class ConnectionError(Exception):
    def __init__(self, status_code, message=None):
        self.status_code = status_code
        self.message = message
        super().__init__(f'status_code: {status_code}, message: {self.message}')
  
class UnexpectedResponse(Exception):
    def __init__(self, status_code, message=None):
        self.status_code = status_code
        self.message = message
        super().__init__(f'status_code: {status_code}, message: {self.message}')
  
class NoSuchDataSource(Exception):
    def __init__(self):
        super().__init__('No Such data source exists')      

class PoliciesNotFound(Exception):
    def __init__(self):
        super().__init__('No policies found in BigID matching request')
        
class PolicyWriteError(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(f'Failed to write policy: {self.message}')  
        
class UserMethodError(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(f'UserMethodError: {self.message}')       

class ClassifierError(Exception):
    def __init__(self, message=None):
        self.message = message
        super().__init__(f'Unknown classifier retrieved: {self.message}')   