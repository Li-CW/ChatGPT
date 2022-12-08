"""
setting中的配置默认为sqlite3数据库 当需要修改成MySql时
并且在setting.py的同级目录的__init__.py 加入如下配置
否则会报错： Error loading MySQLdb module.
"""
import pymysql
pymysql.install_as_MySQLdb()
