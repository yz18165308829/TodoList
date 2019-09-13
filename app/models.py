"""
Date: 2019--08 16:42
User: yz
Email: 1147570523@qq.com
Desc:

"""
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin
from . import  login_manager

# class Role(db.Model):
#     """用户类型"""
#     __tablename__ = 'roles'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), unique=True)
#     users = db.relationship('User', backref='role')
#
#     def __repr__(self):
#         return '<Role % r>' % self.name


class User(UserMixin,db.Model):
    """用户"""
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))  # 加密的密码
    # role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    # 电子邮件地址email,相对于用户名而言,用户更不容易忘记自己的电子邮件地址。
    email = db.Column(db.String(64), unique=True, index=True)
    #用户密码不可以直接访问
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    #设置密码
    @password.setter  #user.password=='westos'
    def password(self, password):
        # generate_password_hash(password, method= pbkdf2:sha1 , salt_length=8):密码加密的散列值。
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        # check_password_hash(hash, password) :密码散列值和用户输入的密码是否匹配.
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User % r>' % self.username


@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))