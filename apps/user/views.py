from flask import Blueprint, render_template, request

from apps.ext import db
from apps.user.models import User

user = Blueprint('user', __name__)


# connection
@user.route('/add/')
def add():
    # user = User(username='吉泽明步', price=9.99)
    # db.session.add(user)
    # db.session.commit()
    # 批量添加
    db.session.add_all([User(username='宫地蓝', price=9.99), User(username='彩美旬果', price=9.99)])
    db.session.commit()
    return '添加操作'


# 查询
@user.route('/find/')
def find():
    #  select * from  user
    users = User.query.all()
    return render_template('users.html', users=users)


@user.route('/detail/')
def find_filter():
    uid = request.args.get('uid')
    user = User.query.filter(User.username == '吉泽明步').first()
    # filter_by 只支持关键字参数
    user = User.query.filter_by(username='吉泽明步').first()
    # get方法只能查询主键
    # 如果没有返回none
    user = User.query.get(uid)
    # 抛出404异常
    # user = User.query.get_or_404(uid)
    return ''


@user.route('/update/')
def update():
    return ''
