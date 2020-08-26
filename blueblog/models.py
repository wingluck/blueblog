# -*- coding=utf-8 -*-

from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash

from blueblog.extensions import db

class AdminUser(db.Model,UserMixin):
    __tablename__='admins'
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(40),nullable=False,index=True)
    password_hash=db.Column(db.String(128))
    blog_title=db.Column(db.String(60))
    blog_sub_title=db.Column(db.String(120))
    name=db.Column(db.String(60))
    about=db.Column(db.Text)

    @property.setter
    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

#博客文章类别
class Category(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(60))

    #与模型Post建立一对多关系
    posts=db.relationship('Post',back_populates='category')

#博客文章
class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    blog_title=db.Column(db.String(60))
    body=db.Column(db.Text)
    timestamp=db.Column(db.DateTime,default=datetime.utcnow)

    category_id=db.Column(db.Integer,db.ForeignKey('Category.id'))
    category=db.relationship('Category',back_populates='posts')

    #建立文章与评论的一对多关系
    #当文章删除时，该篇文章所有的评论也一并删除
    comments=db.relationship('Comment',back_populates='post',cascade='all,delete-orphan')


#文章评论
class Comment(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    author=db.Column(db.String(40))
    email=db.Column(db.String(256))
    site=db.Column(db.String(255))
    timestamp=db.Column(db.DateTime,default=datetime.utcnow,index=True)
    body=db.Column(db.Text)
    from_admin=db.Column(db.Boolean,default=False) #是否是管理员评论
    reviewed=db.Column(db.Boolean,default=False)  #是否通过审核，为了防止垃圾评论或者是不当的评论

    post_id=db.Column(db.Integer,db.ForeignKey('Post.id'))
    post=db.relationship('Post',back_populates='comments')

    replied_id=db.Column(db.Integer,db.ForeignKey('Comment.id'))
    replied=db.relationship('Comment',back_populates='replies',remote_site=[id])  #子评论
    replies=db.relationship('Comment',back_populates='replied',cascade='all,delete-orphan')  #父评论，对应多个子评论

class Link(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(40))
    url=db.Column(db.String(255))




