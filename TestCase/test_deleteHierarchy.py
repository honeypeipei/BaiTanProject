# @File  : test_deleteHierarchy.py
# @Author: leipei
# @Date  :  2020/06/30

import allure
import pytest

from Common.SqlResult import SqlResult

from Common import Consts
from Common import Request
from Common.Session import Session
from Conf.Config import Config
from Params.ParamsHierarchy.paramsHierarchy import  DeleteHierarchy
from Common import Log
import allure
import json
from Common.Assert import Assertions
import time


@allure.feature('DeleteHierarchy')
class TestDeletehierarchy:

    @allure.severity('blocker')
    @allure.story("新增组织机构")
    def test_hierarchy_01(self):
        """
            用例描述：新增组织机构
        """

        #写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已开始执行')
            conf = Config()
            data = DeleteHierarchy()

        #获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[0]
        header = data.header[0]
        param = data.data[0]
        my_param = param[0]['id']
        # my_param = list(param[0].values())
        # print(json.dumps(my_param))
        # print(my_param[0])

        #请求接口
        api_url = req_url + urls
        print(api_url)

        #post请求
        request = Request.Request()
        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
            response = request.post_request(api_url, json.dumps(my_param), header)
            print(response)