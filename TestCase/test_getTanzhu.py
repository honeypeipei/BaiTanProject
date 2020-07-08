# @File  : test_getTanzhu.py
# @Author: leipei
# @Date  :  2020/07/08

import allure
import pytest

from Common.SqlResult import SqlResult

from Common import Consts
from Common import Request
from Common.Session import Session
from Conf.Config import Config
from Params.ParamsUserinfo.paramsUser import  getTanzhu
from Common import Log
import allure
import json
from Common.Assert import Assertions
import time

@allure.feature('getTanzhu')
class Testgetproduct:

    @allure.severity('blocker')
    @allure.story('获取摊主详情')
    def test_hierarchy_01(self):
        """
            用例描述：查看摊主详情
        """

        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已经开始执行')
            conf = Config()
            data = getTanzhu()

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
        api_url = req_url + urls + '/' + params[0]['customerId']
        print(api_url)

        with allure.step("开始请求接口,RUL: {0},header:{1}".format(api_url, header)):
            response = request.get_request(api_url, None, header)

        print(response)

        # 数据库查询结果
        # try:
        #     responsesqlresult = SqlResult(responsesql, env).get_sqlresult_list()
        #     with allure.step("获取预期结果值成功"):
        #         log.info('查询结果数据库成功：' + responsesql)
        # except:
        #     log.info('查询结果数据库失败：' + responsesql)
        #
        # print(response)
        #
        #
        # assert response['code'] == responsecode[0]