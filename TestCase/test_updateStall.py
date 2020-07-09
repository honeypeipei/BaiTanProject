# @File  : test_updateStall.py
# @Author: leipei
# @Date  :  2020/07/09

import allure
import pytest

from Common.SqlResult import SqlResult

from Common import Consts
from Common import Request
from Common.Session import Session
from Conf.Config import Config
from Params.ParamsStall.paramsStall import  UpdateStall
from Common import Log
import allure
import json
from Common.Assert import Assertions
import time


@allure.feature('updateStall')
class TestUpdateStall:

    @allure.severity('blocker')
    @allure.story("1.更新摊位信息")
    def test_updatestall_01(self):
        """
            用例描述：1.更新摊位信息
        """

        #写log
        with allure.step("写入Log"):
            log = Log.MyLog()
            log.info('文件已开始执行')
            conf = Config()
            data = UpdateStall()

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

        # #参数化请求参数
        # with allure.step("获取输入参数值"):
        #     try:
        #         param[0]['productName'] = '只传商品名称' + str(int(time.time()))
        #     except:
        #         log.info("获取参数失败：{0}".format(param[0]))

        #请求接口
        api_url = req_url + urls
        print(api_url)

        #post请求
        request = Request.Request()
        with allure.step("开始请求接口,RUL: {0},header:{1},request:{2}".format(api_url, header, param[0])):
            response = request.post_request(api_url, json.dumps(param[0]), header)
            print(response)