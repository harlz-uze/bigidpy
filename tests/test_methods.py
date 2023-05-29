from policy_engine import dump_policies
import bigid

URL = "https://sandbox.bigiddemo.com"
TEST_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiJiaGFybGV5QGJpZ2lkLmNvbSIsImlzQWRtaW4iOmZhbHNlLCJyb2xlSWRzIjpbIjViNjlhNzg4Y2EzYzllMDAxMDFkYWY4YiIsIjYzMTA1YjUyMDQ1OGZlMDAxM2QxYmM4ZSIsIjVmN2NhMDkzMDE1YjVhMDAxODQ3MWM2ZCIsIjVmN2NhMGE2MDE1YjVhMDAxODQ3MWM2ZSIsIjYxZmQzZWNiYjU0NDlkMDAxNGNlNmJiNyJdLCJyb2xlcyI6W10sInR5cGUiOiJyZWZyZXNoLXRva2VuIiwidG9rZW5OYW1lIjoiMjBiZjVjYzUtMTU2Yy00MTQ0LTlhNzQtZTU2NWU1MmNhODdmIiwidGVuYW50SWQiOiJTSU5HTEVfVEVOQU5UIiwidXVpZCI6bnVsbCwiaWF0IjoxNjg1MDc1MDY1LCJleHAiOjE2ODc2NjcwNjV9.yten7R12_CgLWsO57JzDimBAMcmkQf7ZR1ZFHpXj56c"

class TestMethods:
    def test_dump_poicies_pass(self):
        ''' Test we can dump the policies '''
        connection = bigid.BigID(host=URL, port=443, refresh_token=TEST_TOKEN)
        connection.request_refresh_token()
        test = dump_policies(bigid=connection)
        assert test is not None