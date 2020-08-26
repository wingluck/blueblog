#  -*- coding: utf-8 -*-
import os

from flask import Flask,render_template

from settings import config
from blueblog.extensions import db,bootstrap,moment,mail
from .blueprints.auth import auth_bp
from .blueprints.admin import admin_bp
from .blueprints.blog import blog_bp

def create_app(config_name=None):
    #if config_name is None:
        #config_name = os.getenv('FLASK_CONFIG', 'development')

    #app = Flask('blueblog')
    app = Flask(__name__)
    #对比app=Flask(__name__)的不同
    app.config.from_object(config[config_name])

    register_logging(app)
    register_extentsion(app)
    register_blueprint(app)
    register_errors(app)
    register_commands(app)
    register_templates_context(app)


    return app

#注册日志处理
def register_logging(app):
    pass

#注册扩展
def register_extentsion(app):
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    mail.init_app(app)

#注册模板
def register_blueprint(app):
    app.register_blueprint(auth_bp,url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(blog_bp)

#注册错误处理函数
def register_errors(app):
    @app.errorhandler(400)
    def bad_request(e):
        return render_template('errors/400.html'),400

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'),404

    @app.errorhandler(500)
    def internal_error(e):
        return render_template('errors/500.html'),500

#注册命令
def register_commands(app):
    pass

#注册模板处理
def register_templates_context(app):
    pass



