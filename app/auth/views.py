"""
Date: 2019--08 16:42
User: yz
Email: 1147570523@qq.com
Desc:

"""
from . import auth


@auth.route('/login')
def login():
    return 'login'


@auth.route('/logout')
def logout():
    return 'logout'
