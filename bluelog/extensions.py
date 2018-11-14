# _*_ coding: utf-8 _*_


from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect


bootstrap = Bootstrap()
db = SQLAlchemy()
ckeditor = CKEditor()
csrf = CSRFProtect()
login_manager = LoginManager()
mail = Mail()
migrate = Migrate()
moment = Moment()


@login_manager.user_loader
def load_user(user_id):
    from bluelog.models import Admin
    user = Admin.query.get(int(user_id))
    return user


login_manager.login_view = 'auth.login'
login_manager.login_message = 'Please login to access this message.'
login_manager.login_message_category = 'warning'
