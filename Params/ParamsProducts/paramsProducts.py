# @File  : paramsProducts.py
# @Author: leipei
# @Date  :  2020/07/08

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


class GetProduct:
    log.info('解析yaml, Path:' + path_dir + '/Param/Product/Yaml/getProduct.yaml')
    params = get_parameter('GetProduct','/Params/Param/Product')
    url = params[0]['url']
    header = params[0]['header']
    responsecode = params[0]['responsecode']
    responsesql = params[0]['responsesql']

class AddProducts:
    log.info('解析yaml, Path:' + path_dir + '/Param/Product/Yaml/addProduct.yaml')
    params = get_parameter('AddProduct','/Params/Param/Product')
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