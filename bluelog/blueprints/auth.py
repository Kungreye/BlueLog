#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


from flask import Blueprint

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    return 'The login page'


@auth_bp.route('/logout')
def logout():
    return 'Logout'
