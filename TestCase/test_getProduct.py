# @File  : test_getProduct.py
# @Author: leipei
# @Date  :  2020/07/08


import allure
import pytest

from Common.SqlResult import SqlResult

from Common import Consts
from Common import Request
from Common.Session import Session
from Conf.Config import Config
from Params.ParamsProducts.paramsProducts import  GetProduct
from Common import Log
import allure
import json
from Common.Assert import Assertions
import time

@allure.feature('GetProduct')
class Testgetproduct:

    @allure.severity('blocker')
    @allure.story('获取商品列表')
    def test_hierarchy_01(self):
        """
            用例描述：获取商品列表
        """

        # 写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已经开始执行')
            conf = Config()
            data = GetProduct()

        request = Request.Request()

        # 获取请求域名
        host = conf.host_debug
        req_url = 'http://' + host

        # 获取请求参数
        urls = data.url
        # params = data.data
        header = data.header
        # requestsql = data.selectsql
        env = conf.environment
        responsecode = data.responsecode
        responsesql = data.responsesql
        # casedescription = data.casedec


        # 请求接口
        api_url = req_url + urls

        with allure.step("开始请求接口,RUL: {0},header:{1}".format(api_url, header)):
            response = request.get_request(api_url, None, header)

        # 数据库查询结果
        try:
            responsesqlresult = SqlResult(responsesql, env).get_sqlresult_list()
            with allure.step("获取预期结果值成功"):
                log.info('查询结果数据库成功：' + responsesql)
        except:
            log.info('查询结果数据库失败：' + responsesql)


        assert response['code'] == responsecode