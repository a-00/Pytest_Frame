import requests
import allure
import pytest

@allure.epic("Z05")
@allure.feature("管理中台")
@allure.story("组织机构管理")
class Test_ZZJG():

    @allure.title("组织机构list接口")
    def test_zzjglist(args):
        url = 'http://192.168.100.119:20100/api/xpaas-system/role/detail?id=1123598816738675201'
        token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE3MjEyOTQ5ODgsImNsaWVudF9pZCI6IjAwMDAwMCIsInVzZXJfaWQiOjExMjM1OTg4MjE3Mzg2NzUyMDEsInRlbmFudF9pZCI6IjAwMDAwMCIsImRlcHRfaWQiOiIwIiwiZGVwdF9hbmNlc3RvcnMiOiIiLCJyb2xlX2lkIjoiMTEyMzU5ODgxNjczODY3NTIwMSIsImFjY291bnQiOiJhZG1pbiIsInJvbGVfbmFtZSI6ImFkbWluaXN0cmF0b3IiLCJ1c2VyX25hbWUiOiLotoXnuqfnrqHnkIblkZgiLCJ2IjoiNjYxNzM1ZjBmODAwNDBmYTljYWIxMWQ1OGNkMmQ1N2EiLCJ1bml0X2lkIjowLCJ1bml0X2dyYWRlIjoiIiwiZGF0YV9zY29wZSI6MSwiaXNzIjoic3NvIn0.qW6N-baLusurnOeCeq6ZMPcWpLXR0yXavQ5amHK1MYw'
        headers = {
            'Xpaas-Auth': f'bearer {token}'
        }
        response = requests.get(url, headers = headers)
        assert (response.status_code == 200)