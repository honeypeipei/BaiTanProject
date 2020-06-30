# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午11:32
# @Author  : Grady
# @File    : datas.py

"""
定义所有测试数据

"""
import os

from Common import Log
from Params import tools

log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param





class GetHierarchy:
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Hierarchy.yaml')
    params = get_parameter('GetHierarchy')
    url = params[0]['url']
    header = params[0]['header']
    responsecode = params[0]['responsecode']
    responsesql = params[0]['responsesql']

class AddHierarchy:
    log.info('解析yaml, Path:' + path_dir + '/Params/Yaml/Hierarchy.yaml')
    params = get_parameter('AddHierarchy')
    url = []
    data = []
    header = []
    # selectsql = []
    # responsesql = []
    # responsecode = []
    casedec = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
        # selectsql.append(params[i]['selectsql'])
        # responsesql.append(params[i]['responsesql'])
        # responsecode.append(params[i]['responsecode'])
        casedec.append(params[i]['casedec'])




