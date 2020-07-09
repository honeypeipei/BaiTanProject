# @File  : test_scanArea.py
# @Author: leipei
# @Date  :  2020/07/09

import allure
import pytest

from Common.SqlResult import SqlResult

from Common import Consts
from Common import Request
from Common.Session import Session
from Conf.Config import Config
from Params.ParamsArea.paramsArea import  ScanArea
from Common import Log
import allure
import json
from Common.Assert import Assertions
import time

@allure.feature('ScanArea')
class Testgetuserstatus:

    @allure.severity('blocker')
    @allure.story('扫商圈码')
    def test_scanArea_01(self):
        """
            用例描述：1.已认证已填写摊位信息的用户扫商圈码
        """

        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已经开始执行')
            conf = Config()
            data = ScanArea()

        request = Request.Request()

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[0]
        params = data.data[0]
        header = data.header[0]
        # requestsql = data.selectsql
        env = conf.environment
        responsecode = data.responsecode[0]
        responsesql = data.responsesql[0]
        # casedescription = data.casedec


        # 请求接口
        # api_url = req_url + urls + '/' + params[0]['customerId']
        api_url = req_url + urls
        print(api_url)

        with allure.step("开始请求接口,RUL: {0},header:{1}".format(api_url, header)):
            response = request.get_request(api_url, params[0], header)

        print(response)