# -*- coding:utf-8 -*-
"""
    :author:wingluck
    :date:2020-08-26
"""
import os
import sys

basedir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

class BaseConfig(object):
    SECRET_KEY=os.getenv('SECRET_KEY','wing luck blueblog')

    #SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #邮箱配置
    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('wingluck', os.getenv('MAIL_USERNAME'))
    FLASK_ADMIN = '1293691211@qq.com'

#定义不同环境使用的配置
class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI='sqlite:////'+os.path.join(basedir),'data-dev.db'

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_PRODUCTION_DATABASE_URI')

config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,

    'default':DevelopmentConfig
}