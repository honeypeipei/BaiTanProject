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
from Params.ParamsHierarchy.paramsHierarchy import  EnableHierarchy
from Common import Log
import allure
import json
from Common.Assert import Assertions
import time


@allure.feature('EnableHierarchy')
class TestEnablehierarchy:

    @allure.severity('blocker')
    @allure.story("正常停用一个组织")
    def test_enablehierarchy_01(self):
        """
            用例描述：正常停用一个组织
        """

        #写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已开始执行')
            conf = Config()
            data = EnableHierarchy()

        #获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[0]
        header = data.header[0]
        param = data.data[0]
        selectsql = data.selectsql[0]
        responsecode = data.responsecode[0]
        env = conf.environment

        ids = SqlResult(selectsql, env).get_sqlresult()

        # 参数化请求参数
        with allure.step("获取输入参数值"):
            try:
                param[0]['ids'].append(ids['id'])
            except:
                log.info("获取参数失败：{0}".format(param[0]))

        #请求接口
        api_url = req_url + urls
        print(api_url)
        print(param[0])

        #post请求
        request = Request.Request()
        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
            response = request.post_request(api_url, json.dumps(param[0]), header)
            print(response)

        # 增加断言
        with allure.step("接口返回结果：{0}".format(response)):
            if response['code'] == responsecode:
                assertbody = Assertions()
                assertbody.assert_text(response['body'], True)

    @allure.severity('blocker')
    @allure.story("正常停用多个组织")
    def test_enablehierarchy_02(self):
        """
            用例描述：正常停用多个组织
        """

        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已开始执行')
            conf = Config()
            data = EnableHierarchy()

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[1]
        header = data.header[1]
        param = data.data[1]
        selectsql = data.selectsql[1]
        responsecode = data.responsecode[1]
        env = conf.environment

        ids = SqlResult(selectsql, env).get_sqlresult_list()

        myid = []
        for i in range(len(ids)):
            for k, v in ids[i].items():
                myid.append(ids[i][k])
        print(myid)


        # 参数化请求参数
        with allure.step("获取输入参数值"):
            try:
                param[0]['ids'].extend(myid)
            except:
                log.info("获取参数失败：{0}".format(param[0]))

        # 请求接口
        api_url = req_url + urls

        # post请求
        request = Request.Request()
        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
            response = request.post_request(api_url, json.dumps(param[0]), header)
            print(response)

        # 增加断言
        with allure.step("接口返回结果：{0}".format(response)):
            if response['code'] == responsecode:
                assertbody = Assertions()
                assertbody.assert_text(response['body'], True)