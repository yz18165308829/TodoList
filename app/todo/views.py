"""
Date: 2019--08 16:44
User: yz
Email: 1147570523@qq.com
Desc:

"""
from . import  todo

@todo.route('/add/')
def add():
   return  'todo add'

@todo.route('/delete/')
def delete():
   return  'todo delete'