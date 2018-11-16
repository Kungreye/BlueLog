# _*_ coding: utf-8 _*_

import unittest

from flask import url_for

from bluelog import create_app
from bluelog.extensions import db
from bluelog.models import Admin


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        app = create_app('testing')
        self.context = app.test_request_context()
        self.context.push()
        self.client = app.test_client()
        self.runner = app.test_cli_runner()

        db.create_all()
        user = Admin(
            username='Jeremy',
            blog_title='Testlog',
            blog_sub_title='Test Sub Title',
            name='Jeremy Lin',
            about='Test About'
        )
        user.set_password('12345678')   # LoginForm: password -> length(8, 128)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.drop_all()
        self.context.pop()

    def login(self, username=None, password=None):
        if username is None and password is None:
            username = 'Jeremy'
            password = '12345678'

        return self.client.post(url_for('auth.login'), data=dict(
            username=username,
            password=password,
        ), follow_redirects=True)

    def logout(self):
        return self.client.get(url_for('auth.logout'), follow_redirects=True)
