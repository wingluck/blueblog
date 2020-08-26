from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment

bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
db = SQLAlchemy()
