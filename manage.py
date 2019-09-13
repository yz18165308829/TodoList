"""
Date: 2019--08 16:49
User: yz
Email: 1147570523@qq.com
Desc:
"""
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell
from app import create_app, db
from app import models

app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
   return dict(app=app, db=db)
# 初始化 Flask-Script、Flask-Migrate 和为 Python shell 定义的上下文。
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

# manager.command 修饰器让自定义命令变得简单。修饰函数名就是命令名,函数的文档字符串会显示在帮助消息中。
@manager.command
def test():
   """Run the unit tests."""
   import unittest
   tests = unittest.TestLoader().discover('tests')
   unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
   manager.run()