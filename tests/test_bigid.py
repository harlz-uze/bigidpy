from bigid import BigID
import requests

URL = "https://sandbox.bigiddemo.com"
TEST_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJiaGFybGV5QGJpZ2lkLmNvbSIsImlzQWRtaW4iOmZhbHNlLCJyb2xlSWRzIjpbIjViNjlhNzg4Y2EzYzllMDAxMDFkYWY4YiIsIjYzMTA1YjUyMDQ1OGZlMDAxM2QxYmM4ZSIsIjVmN2NhMDkzMDE1YjVhMDAxODQ3MWM2ZCIsIjVmN2NhMGE2MDE1YjVhMDAxODQ3MWM2ZSIsIjYxZmQzZWNiYjU0NDlkMDAxNGNlNmJiNyIsIjViNjlhNzg4Y2EzYzllMDAxMDFkYWY4ZSJdLCJyb2xlcyI6W10sInR5cGUiOiJyZWZyZXNoLXRva2VuIiwidG9rZW5OYW1lIjoiNGQ3Mjk2MTQtZmQyNC00MzA4LWJjZTQtMDZkMGM2OGU1ZTgyIiwidGVuYW50SWQiOiJTSU5HTEVfVEVOQU5UIiwidXVpZCI6bnVsbCwiaWF0IjoxNjg0OTc3NjQxLCJleHAiOjE2ODc1Njk2NDF9.IQHRjwFdPSO-DZcuQCyPYc3E5k-MWXZ6lyRRzDMMQts"

def mock_convert_response(url, headers, verify):
    ''' Mock a response'''
    r = requests.Response
    r.status_code == 200
    r.json = {'success': True, 'systemToken': 'blahblahblah'}
    return r

class TestRefreshToken:
    def test_token_pass(self, monkeypatch):
        ''' Test a token request '''
        monkeypatch.setattr("requests.get", mock_convert_response)
        test = BigID(host=URL, port=443, refresh_token=TEST_TOKEN)
        assert test.session_token is not None