from policy_engine import dump_policies
from datasource_engine import get_datasource
from data_types import BigData
import bigid

import pytest

URL = "https://sandbox.bigiddemo.com"
TEST_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJiaGFybGV5QGJpZ2lkLmNvbSIsImlzQWRtaW4iOmZhbHNlLCJyb2xlSWRzIjpbIjViNjlhNzg4Y2EzYzllMDAxMDFkYWY4YiIsIjYzMTA1YjUyMDQ1OGZlMDAxM2QxYmM4ZSIsIjVmN2NhMDkzMDE1YjVhMDAxODQ3MWM2ZCIsIjVmN2NhMGE2MDE1YjVhMDAxODQ3MWM2ZSIsIjYxZmQzZWNiYjU0NDlkMDAxNGNlNmJiNyJdLCJyb2xlcyI6W10sInR5cGUiOiJyZWZyZXNoLXRva2VuIiwidG9rZW5OYW1lIjoiMjBiZjVjYzUtMTU2Yy00MTQ0LTlhNzQtZTU2NWU1MmNhODdmIiwidGVuYW50SWQiOiJTSU5HTEVfVEVOQU5UIiwidXVpZCI6bnVsbCwiaWF0IjoxNjg1MDc1MDY1LCJleHAiOjE2ODc2NjcwNjV9.yten7R12_CgLWsO57JzDimBAMcmkQf7ZR1ZFHpXj56c"


@pytest.fixture
def get_connection():
        connection = bigid.BigID(host=URL, port=443, refresh_token=TEST_TOKEN)
        connection.request_refresh_token()
        return connection

class TestPolicyMethods:
    def test_dump_poicies_pass(self, get_connection):
        ''' Test we can dump the policies '''
        test = dump_policies(bigid=get_connection)
        assert test is not None

class TestDataSourceMethods:
    def test_get_datasources(self, get_connection):
        ''' Test we can collect the defined data soufces '''
        test = get_datasource(get_connection)
        assert isinstance(test, BigData)