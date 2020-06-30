# @File  : test_gethierarchy.py
# @Author: leipei
# @Date  :  2020/06/29


import allure
import pytest

from Common.SqlResult import SqlResult

from Common import Consts
from Common import Request
from Common.Session import Session
from Conf.Config import Config
from Params.params import GetHierarchy
from Common import Log
import allure
import json
from Common.Assert import Assertions
import time


@allure.feature('GetHierarchy')
class Testgethierarchy:

    @allure.severity('blocker')
    @allure.story("获取目录")
    def test_hierarchy_01(self):
        """
            用例描述：获取目录
        """

        #写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已开始执行')
            conf = Config()
            data = GetHierarchy()

        #获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url
        header = data.header

        #请求接口
        api_url = req_url + urls
        print(api_url)

        request = Request.Request()
        response = request.get_request(api_url, None, header)
        print(response)