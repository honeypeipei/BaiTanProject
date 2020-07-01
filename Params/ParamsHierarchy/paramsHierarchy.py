# @File  : paramsHierarchy.py
# @Author: leipei
# @Date  :  2020/06/30


import os

from Common import Log
from Params import tools

log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
print(path_dir)


def get_parameter(name,dir):
    data = tools.GetPages().get_page_list(dir)
    param = data[name]
    return param


class GetHierarchy:
    log.info('解析yaml, Path:' + path_dir + '/Param/Hierarchy/Yaml/GetHierarchy.yaml')
    params = get_parameter('GetHierarchy','/Params/Param/Hierarchy')
    url = params[0]['url']
    header = params[0]['header']
    responsecode = params[0]['responsecode']
    responsesql = params[0]['responsesql']

class AddHierarchy:
    log.info('解析yaml, Path:' + path_dir + '/Param/Hierarchy/Yaml/AddHierarchy.yaml')
    params = get_parameter('AddHierarchy','/Params/Param/Hierarchy')
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

class DeleteHierarchy:
    log.info('解析yaml, Path:' + path_dir + '/Param/Hierarchy/Yaml/DeleteHierarchy.yaml')
    params = get_parameter('DeleteHierarchy','/Params/Param/Hierarchy')
    url = []
    data = []
    header = []
    selectsql = []
    responsesql = []
    responsecode = []
    casedec = []
    responsemessage = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
        selectsql.append(params[i]['selectsql'])
        responsesql.append(params[i]['responsesql'])
        responsecode.append(params[i]['responsecode'])
        responsemessage.append(params[i]['responsemessage'])
        casedec.append(params[i]['casedec'])

class EnableHierarchy:
    log.info('解析yaml, Path:' + path_dir + '/Param/Hierarchy/Yaml/EnableHierarchy.yaml')
    params = get_parameter('EnableHierarchy','/Params/Param/Hierarchy')
    url = []
    data = []
    header = []
    selectsql = []
    responsesql = []
    responsecode = []
    casedec = []
    responsemessage = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
        selectsql.append(params[i]['selectsql'])
        responsesql.append(params[i]['responsesql'])
        responsecode.append(params[i]['responsecode'])
        responsemessage.append(params[i]['responsemessage'])
        casedec.append(params[i]['casedec'])

class UpdateHierarchy:
    log.info('解析yaml, Path:' + path_dir + '/Param/Hierarchy/Yaml/UpdateHierarchy.yaml')
    params = get_parameter('UpdateHierarchy','/Params/Param/Hierarchy')
    url = []
    data = []
    header = []
    selectsql = []
    responsesql = []
    responsecode = []
    casedec = []
    responsemessage = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
        selectsql.append(params[i]['selectsql'])
        responsesql.append(params[i]['responsesql'])
        responsecode.append(params[i]['responsecode'])
        responsemessage.append(params[i]['responsemessage'])
        casedec.append(params[i]['casedec'])

class SecondHierarchy:
    log.info('解析yaml, Path:' + path_dir + '/Param/Hierarchy/Yaml/SecondLevalHierarchy.yaml')
    params = get_parameter('SecondHierarchy','/Params/Param/Hierarchy')
    url = params[0]['url']
    header = params[0]['header']
    # responsecode = params[0]['responsecode']
    responsesql = params[0]['responsesql']