"""
Date: 2019--08 16:44
User: yz
Email: 1147570523@qq.com
Desc:
"""
from flask import Blueprint

# 实例化一个 Blueprint 类对象可以创建蓝本, 指定蓝本的名字和蓝本所在的包或模块
todo = Blueprint('todo', __name__)
# 把路由和错误处理程序与蓝本关联, 一定要写在最后, 防止循环导入依赖;
from . import views, errors
