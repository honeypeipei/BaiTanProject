# @File  : Config.py
# @Author: leipei
# @Date  :  2020/06/29

import os
from configparser import ConfigParser

from Common import Log


class Config:
    # titles:
    TITLE_DEBUG = "private_debug"
    TITLE_RELEASE = "online_release"
    TITLE_EMAIL = "mail"

    # values:
    # [debug\release]
    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environment"
    VALUE_VERSION_CODE = "versionCode"
    VALUE_HOST = "host"
    # VALUE_LOGIN_HOST = "loginHost"

    # VALUE_PORT_COMMON_SERVICE= "portCommonService"
    # VALUE_PORT_CONFIG_SERVICE = "portConfigService"
    # VALUE_PORT_MALL_SERVICE = "portMallService"
    # VALUE_PORT_SHOP_SERVICE = "portShopService"
    # VALUE_PORT_MALL_STANDARD_SERVICE = "portMallStandardService"
    # VALUE_PORT_SALE_SERVICE = "portSaleService"
    # VALUE_PORT_USER_SERVICE ="portUserService"

    # VALUE_LOGIN_INFO = "loginInfo"
    # VALUE_LOGIN_HEADER="loginheaders"
    VALUE_SQLHOST = "sqlhost"
    VALUE_SQLUSER ="sqluser"
    VALUE_SQLPASSWORD ="sqlpassword"
    VALUE_DATABASE = "sqldatabase"
    VALUE_SQLPORT='sqlport'
    # [mail]
    VALUE_SMTP_SERVER = "smtpserver"
    VALUE_SENDER = "sender"
    VALUE_RECEIVER = "receiver"
    VALUE_USERNAME = "username"
    VALUE_PASSWORD = "password"

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir+'/Report/xml'
        self.html_report_path = Config.path_dir+'/Report/html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')
        print()

        self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.environment = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
        self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
        self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
        # self.loginHost_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_HOST)
        # self.loginInfo_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_INFO)
        # self.loginheader_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_HEADER)

        self.sql_host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_SQLHOST)
        self.sql_user_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_SQLUSER)
        self.sql_password_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_SQLPASSWORD)
        self.sql_database_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_DATABASE)
        self.sql_sqlport_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_SQLPORT)



    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)


