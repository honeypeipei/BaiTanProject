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
from Params.ParamsHierarchy.paramsHierarchy import  GetHierarchy
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
        env = conf.environment
        responsesql = data.responsesql
        responsecode = data.responsecode

        # 获取请求参数
        urls = data.url
        header = data.header

        #请求接口
        api_url = req_url + urls
        request = Request.Request()
        with allure.step("开始请求接口,RUL: {0},header:{1}".format(api_url, header)):
            response = request.get_request(api_url, None, header)
            print(response['body'])

        # 数据库查询结果
        try:
            # print(responsesql)
            responsesqlresult = SqlResult(responsesql, env).get_sqlresult_list()
            print(responsesqlresult)
            with allure.step("获取预期结果值成功"):
                log.info('查询结果数据库成功：' + responsesql)
        except:
            log.info('查询结果数据库失败：' + responsesql)

        print(responsecode)

        # 增加断言
        assertbody = Assertions()
        with allure.step("增加断言，接口返回结果：{0}".format(response)):
            assertbody.assert_text(str(response['code']), str(responsecode))
            if response['code'] == responsecode:
                for i in range(len(responsesqlresult)):
                    for k, v in responsesqlresult[i].items():
                        assertbody.assert_body(response['body'][i], k, responsesqlresult[i][k])