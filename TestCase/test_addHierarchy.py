# @File  : test_addHierarchy.py
# @Author: leipei
# @Date  :  2020/06/30

import allure
import pytest

from Common.SqlResult import SqlResult

from Common import Consts
from Common import Request
from Common.Session import Session
from Conf.Config import Config
from Params.ParamsHierarchy.paramsHierarchy import  AddHierarchy
from Common import Log
import allure
import json
from Common.Assert import Assertions
import time


@allure.feature('GetHierarchy')
class TestAddhierarchy:

    @allure.severity('blocker')
    @allure.story("新增二级组织机构")
    def test_addhierarchy_01(self):
        """
            用例描述：新增组织机构
        """

        #写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已开始执行')
            conf = Config()
            data = AddHierarchy()

        #获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[0]
        header = data.header[0]
        param = data.data[0]
        env = conf.environment
        responsecode = data.responsecode[0]
        responsesql = data.responsesql[0]
        print(param[0])

        #参数化请求参数
        with allure.step("获取输入参数值"):
            try:
                param[0]['name'] = '国联' + str(int(time.time()))
            except:
                log.info("获取参数失败：{0}".format(param[0]))

        #请求接口
        api_url = req_url + urls
        print(api_url)

        #post请求
        request = Request.Request()
        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
            response = request.post_request(api_url, json.dumps(param[0]), header)
            print(response)

        # 数据库查询结果
        try:
            # responsesql = str(responsesql[0]).replace('@sqlresult', str(response['body']['id']))
            responsesqlresult = SqlResult(responsesql, env).get_sqlresult_list()
            with allure.step("获取预期结果值成功，查询Sql：{0},查询结果：{1}".format(responsesql, responsesqlresult)):
                log.info('查询结果数据库成功：' + responsesql)
        except:
            log.info('查询结果数据库失败：' + responsesql)

        actual = []
        for i in range(len(responsesqlresult)):
            for k, v in responsesqlresult[i].items():
                actual.append(responsesqlresult[i][k])

        # 增加断言
        assertbody = Assertions()
        with allure.step("接口返回结果：{0}".format(response)):
            assertbody.assert_text(str(response['code']), str(responsecode))
            if response['code'] == responsecode:
                assert param[0]['name'] in actual


    # @allure.severity('normal')
    # @allure.story('一级name重复')
    # def test_hierarchy_08(self, action):
    #     """
    #         用例描述：一级name重复
    #     """
    #     # 写log
    #     with allure.step("写入Log"):
    #         log = Log.MyLog()
    #         log.info('文件已经开始执行')
    #         conf = Config()
    #         data = CreateHierarchy()
    #
    #     request = Request.Request(action)
    #
    #     # 获取请求域名
    #     host = conf.host_debug
    #     req_url = 'http://' + host
    #
    #     # 获取请求参数
    #     urls = data.url
    #     params = data.data
    #     header = data.header
    #     requestsql = data.selectsql
    #     env = conf.environment
    #     responsecode = data.responsecode
    #     responsesql = data.responsesql
    #     casedescription = data.casedec
    #
    #     # 获取token
    #     token = Session().get_session('debug')
    #     print(token)
    #     dict_token = {'X-Api-Authorization': token}
    #     header = dict(header[7])
    #     header.update(dict_token)
    #     print(header)
    #
    #     # 参数化请求参数
    #     with allure.step("获取输入参数值"):
    #         try:
    #             sqlresult = SqlResult(requestsql[7], env).get_sqlresult()
    #             params[7][0]['name'] = sqlresult['name']
    #         except:
    #             log.info("获取输入参数值失败：{0}".format(params[7][0]))
    #
    #     # 请求接口
    #     api_url = req_url + urls[7]
    #     print(api_url)
    #     print(params[7][0])
    #     print(header)
    #
    #     with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, params[7][0])):
    #         response = request.post_request(api_url, json.dumps(params[7][0]), header)
    #         print(response)
    #
    #     # 增加断言
    #     assertbody = Assertions()
    #     with allure.step("接口返回结果：{0}".format(response)):
    #         assertbody.assert_text(str(response['code']), str(responsecode[7]))
    #         if response['code'] == responsecode[7]:
    #             assertbody = Assertions()
    #             assertbody.assert_text(response['text'], "data.name should NOT be shorter than 1 characters")
    #         else:
    #             log.info('查询结果数据库失败：' + responsesql)


    @allure.severity('blocker')
    @allure.story("创建三级组织")
    def test_addhierarchy_02(self):
        """
            用例描述：创建三级组织
        """

        #写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已开始执行')
            conf = Config()
            data = AddHierarchy()

        #获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[1]
        header = data.header[1]
        param = data.data[1]
        env = conf.environment
        responsecode = data.responsecode[1]
        responsesql = data.responsesql[1]
        selectsql = data.selectsql[1]
        print(param[0])

        parentid = SqlResult(selectsql, env).get_sqlresult()

        # 参数化请求参数
        with allure.step("获取输入参数值"):
            try:
                param[0]['name'] = '国联信息' + str(int(time.time()))
                param[0]['parent_id'] = parentid['id']
            except:
                log.info("获取参数失败：{0}".format(param[0]))

        #请求接口
        api_url = req_url + urls
        print(api_url)

        #post请求
        request = Request.Request()
        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
            response = request.post_request(api_url, json.dumps(param[0]), header)
            print(response)

        # 数据库查询结果
        try:
            responsesql = str(responsesql).replace('@sqlresult', str(parentid['id']))
            responsesqlresult = SqlResult(responsesql, env).get_sqlresult_list()
            with allure.step("获取预期结果值成功，查询Sql：{0},查询结果：{1}".format(responsesql, responsesqlresult)):
                log.info('查询结果数据库成功：' + responsesql)
        except:
            log.info('查询结果数据库失败：' + responsesql)

        actual = []
        for i in range(len(responsesqlresult)):
            for k, v in responsesqlresult[i].items():
                actual.append(responsesqlresult[i][k])

        # 增加断言
        assertbody = Assertions()
        with allure.step("接口返回结果：{0}".format(response)):
            assertbody.assert_text(str(response['code']), str(responsecode))
            if response['code'] == responsecode:
                assert param[0]['name'] in actual