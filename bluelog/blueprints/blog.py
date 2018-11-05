# python3
# _*_ coding: utf-8 _*_


from flask import Blueprint

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/about')
def about():
    return 'The about page'


@blog_bp.route('/category/<int:category_id>')
def category(category_id):
    return 'The category page'
