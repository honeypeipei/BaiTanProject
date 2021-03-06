# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午10:56
# @Author  : Grady
# @File    : tools.py

"""
读取yaml测试数据

"""

import os
import os.path
import yaml


def parse(dir):
    path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + dir
    pages = {}
    for root, dirs, files in os.walk(path_ya):
        for name in files:
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path, 'r',encoding="UTF-8") as f:
                page = yaml.safe_load(f)
                pages.update(page)
        return pages


class GetPages:
    @staticmethod
    def get_page_list(dir):
        _page_list = {}
        pages = parse(dir)
        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []

            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list

        return _page_list


if __name__ == '__main__':
    lists = GetPages.get_page_list()
