# @File  : test_updateHierarchy.py
# @Author: leipei
# @Date  :  2020/07/01

import allure
import pytest

from Common.SqlResult import SqlResult

from Common import Consts
from Common import Request
from Common.Session import Session
from Conf.Config import Config
from Params.ParamsHierarchy.paramsHierarchy import  UpdateHierarchy
from Common import Log
import allure
import json
from Common.Assert import Assertions
import time


@allure.feature('UpdateHierarchy')
class TestUpdatehierarchy:

    @allure.severity('blocker')
    @allure.story("正常更新，不变层级，正常更新名称")
    def test_updatehierarchy_01(self):
        """
            用例描述：正常更新，不变层级，正常更新名称
        """

        #写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已开始执行')
            conf = Config()
            data = UpdateHierarchy()

        #获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[0]
        header = data.header[0]
        param = data.data[0]
        responsecode = data.responsecode[0]
        env = conf.environment
        selectsql = data.selectsql[0]
        parentid = SqlResult(selectsql, env).get_sqlresult()

        # 参数化请求参数
        with allure.step("获取输入参数值"):
            try:
                param[0]['id'] = parentid['id']
                param[0]['name'] = '不变层级，正常更新名称' + str(int(time.time()))
                param[0]['parent_id'] = parentid['parent_id']
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

        # 增加断言
        with allure.step("接口返回结果：{0}".format(response)):
            if response['code'] == responsecode:
                assertbody = Assertions()
                assertbody.assert_text(response['body'], True)

    @allure.severity('blocker')
    @allure.story("正常更新，改变层级，正常更新名称")
    def test_updatehierarchy_02(self):
        """
            用例描述：正常更新，不变层级，正常更新名称
        """

        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已开始执行')
            conf = Config()
            data = UpdateHierarchy()

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[1]
        header = data.header[1]
        param = data.data[1]
        responsecode = data.responsecode[1]
        env = conf.environment
        selectsql = data.selectsql[1]
        sqlpid = data.sqlpid[1]
        parentid = SqlResult(selectsql, env).get_sqlresult()

        sqlname = str(sqlpid).replace('@sqlresult', str(parentid['parent_id']))
        pid = SqlResult(sqlname, env).get_sqlresult()

        # 参数化请求参数
        with allure.step("获取输入参数值"):
            try:
                param[0]['id'] = parentid['id']
                param[0]['name'] = '改变层级更新组织名称' + str(int(time.time()))
                param[0]['parent_id'] = pid['id']
            except:
                log.info("获取参数失败：{0}".format(param[0]))

        # 请求接口
        api_url = req_url + urls
        print(api_url)

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

    @allure.severity('blocker')
    @allure.story("不变层级，名称重复")
    def test_updatehierarchy_03(self):
        """
            用例描述：不变层级，名称重复
        """

        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已开始执行')
            conf = Config()
            data = UpdateHierarchy()

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[2]
        header = data.header[2]
        param = data.data[2]
        responsecode = data.responsecode[2]
        sql_name = data.sqlname[2]
        env = conf.environment
        selectsql = data.selectsql[2]
        errorcode = data.errorcode[2]
        parentid = SqlResult(selectsql, env).get_sqlresult()

        sqlname = str(sql_name).replace('@sqlresult', str(parentid['parent_id']))
        pname = SqlResult(sqlname, env).get_sqlresult()

        # 参数化请求参数
        with allure.step("获取输入参数值"):
            try:
                param[0]['id'] = parentid['id']
                param[0]['name'] = pname['name']
                param[0]['parent_id'] = parentid['parent_id']
            except:
                log.info("获取参数失败：{0}".format(param[0]))

        # 请求接口
        api_url = req_url + urls
        print(api_url)

        print(param[0])

        # post请求
        request = Request.Request()
        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
            response = request.post_request(api_url, json.dumps(param[0]), header)
            print(response)

            # 增加断言
            with allure.step("接口返回结果：{0}".format(response)):
                if response['code'] == responsecode:
                    assertbody = Assertions()
                    assertbody.assert_text(response['body'], errorcode)

    @allure.severity('blocker')
    @allure.story("不变层级，名称重复")
    def test_updatehierarchy_04(self):
        """
            用例描述：不变层级，名称重复
        """

        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已开始执行')
            conf = Config()
            data = UpdateHierarchy()

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[3]
        header = data.header[3]
        param = data.data[3]
        responsecode = data.responsecode[3]
        env = conf.environment
        selectsql = data.selectsql[3]
        sqlpid = data.sqlpid[3]
        errorcode = data.errorcode[3]
        sql_name = data.sqlname[3]

        #随机一个需要更改的组织，取相应id 和 pid
        parentid = SqlResult(selectsql, env).get_sqlresult()

        #随机一个父id不等于null不等于原父id
        sqlname = str(sqlpid).replace('@sqlresult', str(parentid['parent_id']))
        pid = SqlResult(sqlname, env).get_sqlresult()

        #随机一个同父id的name
        psqlname = str(sql_name).replace('@sqlresult', str(pid['parent_id']))
        pname = SqlResult(psqlname, env).get_sqlresult()

        # 参数化请求参数
        with allure.step("获取输入参数值"):
            try:
                param[0]['id'] = parentid['id']
                param[0]['name'] = pname['name']
                param[0]['parent_id'] = pid['parent_id']
            except:
                log.info("获取参数失败：{0}".format(param[0]))

        # 请求接口
        api_url = req_url + urls
        print(api_url)
        print(param[0])

        # post请求
        request = Request.Request()
        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
            response = request.post_request(api_url, json.dumps(param[0]), header)
            print(response)

        # 增加断言
        with allure.step("接口返回结果：{0}".format(response)):
            if response['code'] == responsecode:
                assertbody = Assertions()
                assertbody.assert_text(response['body'], errorcode)