# @File  : paramsStall.py
# @Author: leipei
# @Date  :  2020/07/09

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


class getStall:
    log.info('解析yaml, Path:' + path_dir + '/Param/Tanwei/Yaml/getStall.yaml')
    params = get_parameter('GetStall','/Params/Param/Tanwei')
    url = []
    data = []
    header = []
    selectsql = []
    responsesql = []
    responsecode = []
    casedec = []
    errorcode = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
        selectsql.append(params[i]['selectsql'])
        responsesql.append(params[i]['responsesql'])
        responsecode.append(params[i]['responsecode'])
        casedec.append(params[i]['casedec'])
        errorcode.append(params[i]['errorcode'])

class AddStall:
    log.info('解析yaml, Path:' + path_dir + '/Param/Tanwei/Yaml/addTanwei.yaml')
    params = get_parameter('AddStall','/Params/Param/Tanwei')
    url = []
    data = []
    header = []
    selectsql = []
    responsesql = []
    responsecode = []
    casedec = []
    errorcode = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
        selectsql.append(params[i]['selectsql'])
        responsesql.append(params[i]['responsesql'])
        responsecode.append(params[i]['responsecode'])
        casedec.append(params[i]['casedec'])
        errorcode.append(params[i]['errorcode'])