from bigid import BigID
import requests

URL = "https://54.161.78.47:30443"
TEST_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJiaGFybGV5QGJpZ2lkLmNvbSIsImlzQWRtaW4iOmZhbHNlLCJyb2xlSWRzIjpbIjViNjlhNzg4Y2EzYzllMDAxMDFkYWY4ZSIsIjViNjlhNzg4Y2EzYzllMDAxMDFkYWY4YiJdLCJyb2xlcyI6W10sInR5cGUiOiJyZWZyZXNoLXRva2VuIiwidG9rZW5OYW1lIjoiZDQ5ODJlN2QtMjE5Ni00ZGQ5LTg2NzQtNTUxOTJjZjJiYzc1IiwidGVuYW50SWQiOiJTSU5HTEVfVEVOQU5UIiwidXVpZCI6bnVsbCwiaWF0IjoxNjg1NDk3MjMwLCJleHAiOjE2ODgwODkyMzB9.BlL9FHmiwd3fPe139KzK_-aXsdb4Kw6FSiHqMmt8mA4.IQHRjwFdPSO-DZcuQCyPYc3E5k-MWXZ6lyRRzDMMQts"

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

class TestAuthentication:
    def test_user_password(self):
        ''' Test that we can authenticate and get a token from the system '''
        test = BigID(host=URL, port=443)
        test.authenticate(user='bharley@bigid.com', password='CURthis?')
        assert test.session_token is not None