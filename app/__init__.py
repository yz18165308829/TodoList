"""
Date: 2019--08 16:41
User: yz
Email: 1147570523@qq.com
Desc:

"""
"""
程序工厂函数, 延迟创建程序实例
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from config import config
bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()

import pymysql
pymysql.install_as_MySQLdb()


from flask_login import LoginManager
# .......此处省略前面重复的代码
login_manager = LoginManager()
# session_protection 属性提供不同的安全等级防止用户会话遭篡改。
login_manager.session_protection = 'strong'
# login_view 属性设置登录页面的端点。
login_manager.login_view = 'auth.login'

def create_app(config_name='development'):
   """
  默认创建开发环境的app对象
  """
   app = Flask(__name__)
   app.config.from_object(config[config_name])
   config[config_name].init_app(app)
   bootstrap.init_app(app)
   mail.init_app(app)
   db.init_app(app)

   # 附加路由和自定义的错误页面
   from app.auth import auth
   app.register_blueprint(auth)  # 注册蓝本

   from app.todo import todo
   app.register_blueprint(todo, url_prefix='/todo')  # 注册蓝本

   # 用户认证新加扩展
   login_manager.init_app(app)

   return app




