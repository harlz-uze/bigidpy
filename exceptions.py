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