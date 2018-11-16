#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

from flask import current_app, abort

from tests.base import BaseTestCase


class BasicTestCase(BaseTestCase):

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_404_error(self):
        response = self.client.get('/nothing')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 404)
        self.assertIn('404 Error', data)

    def test_400_error(self):
        @current_app.route('/400')
        def bad_request_error_for_test():
            abort(400)

        response = self.client.get('/400')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 400)
        self.assertIn('400 Error', data)

    def test_500_error(self):
        @current_app.route('/500')
        def internal_server_error_for_test():
            abort(500)

        response = self.client.get('/500')
        data = response.get_data(as_text=True)
        self.assertEqual(response.status_code, 500)
        self.assertIn('500 Error', data)
