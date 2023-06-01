from policy_engine import dump_policies
from datasource_engine import get_datasource
from scanner_engine import get_scanner_status_all
from data_types import BigData
import bigid

import pytest

URL = "https://54.161.78.47:30443"
TEST_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJiaGFybGV5QGJpZ2lkLmNvbSIsImlzQWRtaW4iOmZhbHNlLCJyb2xlSWRzIjpbIjViNjlhNzg4Y2EzYzllMDAxMDFkYWY4ZSIsIjViNjlhNzg4Y2EzYzllMDAxMDFkYWY4YiJdLCJyb2xlcyI6W10sInR5cGUiOiJyZWZyZXNoLXRva2VuIiwidG9rZW5OYW1lIjoiOGNkYzI3OTQtOTI5Yy00MmNlLWIyY2UtOTZiYzEwNzNhNDAxIiwidGVuYW50SWQiOiJTSU5HTEVfVEVOQU5UIiwidXVpZCI6bnVsbCwiaWF0IjoxNjg1NTk4MTQ5LCJleHAiOjE2ODgxOTAxNDl9.6p2-fNY5WcGlPtDaYKjXRZGisZ2SbeiKZdXYAwHSvkk"


def mock_scanner_jobs(bigid):
    data: BigData(status_code=200, data={'result': 'mock result'})
    return data

@pytest.fixture
def get_connection():
        connection = bigid.BigID(host=URL, port=443, refresh_token=TEST_TOKEN)
        connection.request_refresh_token()
        return connection

class TestPolicyMethods:
    def test_dump_poicies_pass(self):
        ''' Test we can dump the policies '''
        connection = bigid.BigID(host=URL, port=443, refresh_token=TEST_TOKEN)
        connection.request_refresh_token()
        assert connection.session_token is not None
        test = dump_policies(bigid=connection)
        assert test is None

class TestDataSourceMethods:
    def test_get_datasources(self, get_connection):
        ''' Test we can collect the defined data soufces '''
        test = get_datasource(get_connection)
        assert isinstance(test, BigData)
        
class TestScannerMethods:
    def test_get_scanner_jobs(self, monkeypatch, get_connection):
        ''' Test that the test scanner job returns data '''
        monkeypatch.setattr('get_scanner_status_all', mock_scanner_jobs)
        test = get_scanner_status_all(bigid=get_connection)
        assert isinstance(test, BigData)