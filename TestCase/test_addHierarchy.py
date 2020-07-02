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

    # @allure.severity('normal')
    # @allure.story('二级name重复')
    # def test_addhierarchy_03(self):
    #     """
    #         用例描述：一级name重复
    #     """
    #     # 写log
    #     with allure.step("写入Log"):
    #         log = Log.MyLog()
    #         log.info('文件已经开始执行')
    #         conf = Config()
    #         data = AddHierarchy()
    #
    #     # 获取请求域名
    #     host = conf.host_debug
    #     req_url = 'http://' + host
    #
    #     # 获取请求参数
    #     urls = data.url[2]
    #     header = data.header[2]
    #     param = data.data[2]
    #     env = conf.environment
    #     responsecode = data.responsecode[2]
    #     responsesql = data.responsesql[2]
    #     selectsql = data.selectsql[2]
    #     print(param[0])
    #
    #     requestname = SqlResult(selectsql, env).get_sqlresult()
    #
    #     # 参数化请求参数
    #     with allure.step("获取输入参数值"):
    #         try:
    #             param[0]['name'] = requestname['name']
    #         except:
    #             log.info("获取参数失败：{0}".format(param[0]))
    #
    #     # 请求接口
    #     api_url = req_url + urls
    #     print(api_url)
    #
    #     # post请求
    #     request = Request.Request()
    #     with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
    #         response = request.post_request(api_url, json.dumps(param[0]), header)
    #         print(response)
    #         #{'code': 200, 'body': '组织的名称已经存在', 'text': '"组织的名称已经存在"', 'time_consuming': 983.588, 'time_total': 0.983588, 'header': {'X-Api-Error-Code': 'HIERARCHY_NAME_IS_EXIST', 'Content-Type': 'application/json', 'Content-Length': '29', 'Date': 'Thu, 02 Jul 2020 02:51:41 GMT'}}
    #
    #     # 增加断言
    #     with allure.step("接口返回结果：{0}".format(response)):
    #         if response['code'] == responsecode:
    #             assertbody = Assertions()
    #             assertbody.assert_text(response['header']['X-Api-Error-Code'], "HIERARCHY_NAME_IS_EXIST")
            # else:
            #     log.info('查询结果数据库失败：' + responsesql)
    #
    # @allure.severity('normal')
    # @allure.story('三级name重复')
    # def test_addhierarchy_04(self):
    #     """
    #         用例描述：三级name重复
    #     """
    #     # 写log
    #     with allure.step("写入Log"):
    #         log = Log.MyLog()
    #         log.info('文件已经开始执行')
    #         conf = Config()
    #         data = AddHierarchy()
    #
    #     # 获取请求域名
    #     host = conf.host_debug
    #     req_url = 'http://' + host
    #
    #     # 获取请求参数
    #     urls = data.url[3]
    #     header = data.header[3]
    #     param = data.data[3]
    #     env = conf.environment
    #     responsecode = data.responsecode[3]
    #     responsesql = data.responsesql[3]
    #     selectsql = data.selectsql[3]
    #
    #     requestname = SqlResult(selectsql, env).get_sqlresult()
    #
    #     # 参数化请求参数
    #     with allure.step("获取输入参数值"):
    #         try:
    #             param[0]['name'] = requestname['name']
    #         except:
    #             log.info("获取参数失败：{0}".format(param[0]))
    #
    #     # 请求接口
    #     api_url = req_url + urls
    #     print(api_url)
    #     print(param[0])
    #
    #     # post请求
    #     request = Request.Request()
    #     with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
    #         response = request.post_request(api_url, json.dumps(param[0]), header)
    #         print(response)
    #
    #     # 增加断言
    #     with allure.step("接口返回结果：{0}".format(response)):
    #         if response['code'] == responsecode:
    #             assertbody = Assertions()
    #             assertbody.assert_text(response['header']['X-Api-Error-Code'], "HIERARCHY_NAME_IS_EXIST")

    @allure.severity('normal')
    @allure.story('name字段缺失')
    def test_addhierarchy_05(self):
        """
            用例描述：name字段缺失
        """
        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已经开始执行')
            conf = Config()
            data = AddHierarchy()

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[2]
        header = data.header[2]
        param = data.data[2]
        env = conf.environment
        responsecode = data.responsecode[2]
        responsesql = data.responsesql[2]
        selectsql = data.selectsql[2]
        errorcode = data.errorcode[2]
        print(param[0])

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
                assertbody.assert_text(response['header']['X-Api-Error-Code'], errorcode)

    @allure.severity('normal')
    @allure.story('name传空')
    def test_addhierarchy_06(self):
        """
            用例描述：name字段传空
        """
        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已经开始执行')
            conf = Config()
            data = AddHierarchy()

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[3]
        header = data.header[3]
        param = data.data[3]
        env = conf.environment
        responsecode = data.responsecode[3]
        responsesql = data.responsesql[3]
        selectsql = data.selectsql[3]
        errorcode = data.errorcode[3]
        print(param[0])

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
                assertbody.assert_text(response['header']['X-Api-Error-Code'], errorcode)

    @allure.severity('normal')
    @allure.story('name传空格')
    def test_addhierarchy_07(self):
        """
            用例描述：name字段传空
        """
        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已经开始执行')
            conf = Config()
            data = AddHierarchy()

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[4]
        header = data.header[4]
        param = data.data[4]
        env = conf.environment
        responsecode = data.responsecode[4]
        responsesql = data.responsesql[4]
        selectsql = data.selectsql[4]
        errorcode = data.errorcode[4]
        print(param[0])

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
                assert response['body']
                assertbody = Assertions()
                assertbody.assert_text(response['header']['X-Api-Error-Code'], errorcode)

    @allure.severity('normal')
    @allure.story('同一层级相同上级name重复')
    def test_addhierarchy_08(self):
        """
            用例描述：同一层级相同上级name重复
        """
        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已经开始执行')
            conf = Config()
            data = AddHierarchy()

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[5]
        header = data.header[5]
        param = data.data[5]
        env = conf.environment
        responsecode = data.responsecode[5]
        responsesql = data.responsesql[5]
        selectsql = data.selectsql[5]

        parentid = SqlResult(selectsql, env).get_sqlresult()

        # 参数化请求参数
        with allure.step("获取输入参数值"):
            try:
                param[0]['parent_id'] = parentid['id']
                param[0]['name'] = '同层级同上级' + str(int(time.time()))
            except:
                log.info("获取参数失败：{0}".format(param[0]))

        # 请求接口
        api_url = req_url + urls
        print(api_url)
        print(param[0])
        request = Request.Request()
        addname = request.post_request(api_url, json.dumps(param[0]), header)

        sqlname = str(responsesql).replace('@sqlresult', str(parentid['id']))
        param[0]['name'] = SqlResult(sqlname, env).get_sqlresult()['name']

        ############################
        print(param[0])

        # post请求

        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
            response = request.post_request(api_url, json.dumps(param[0]), header)
            print(response)

        # 增加断言
        with allure.step("接口返回结果：{0}".format(response)):
            if response['code'] == responsecode:
                assertbody = Assertions()
                assertbody.assert_text(response['header']['X-Api-Error-Code'], "HIERARCHY_NAME_IS_EXIST")

    @allure.severity('normal')
    @allure.story('同一层级不同上级name重复')
    def test_addhierarchy_09(self):
        """
            用例描述：同一层级不同上级name重复
        """
        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已经开始执行')
            conf = Config()
            data = AddHierarchy()

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url[6]
        header = data.header[6]
        param = data.data[6]
        env = conf.environment
        responsecode = data.responsecode[6]
        responsesql = data.responsesql[6]
        sqlparentid = data.sqlpid[6]
        sqlname = data.sqlname[6]
        selectsql = data.selectsql[6]

        parentid = SqlResult(selectsql, env).get_sqlresult()

        # 参数化请求参数
        with allure.step("获取输入参数值"):
            try:
                param[0]['parent_id'] = parentid['id']
                param[0]['name'] = '同层级不同上级' + str(int(time.time()))
            except:
                log.info("获取参数失败：{0}".format(param[0]))

        # 请求接口
        api_url = req_url + urls
        print(api_url)
        print(param[0])
        request = Request.Request()
        addname = request.post_request(api_url, json.dumps(param[0]), header)


        # dsqlname = str(sqlname).replace('@sqlresult', str(parentid['id']))
        sqlid = str(sqlparentid).replace('@sqlresult', str(parentid['id']))
        # param[0]['name'] = SqlResult(dsqlname, env).get_sqlresult()['name']
        param[0]['parent_id'] = SqlResult(sqlid, env).get_sqlresult()['id']

        ############################
        print(param[0])

        # post请求

        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
            response = request.post_request(api_url, json.dumps(param[0]), header)
            print(response)

        # 增加断言
        with allure.step("接口返回结果：{0}".format(response)):
            if response['code'] == responsecode:
                assertbody = Assertions()
                assertbody.assert_text(response['body'], True)

