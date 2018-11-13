#!/usr/bin/env python3
# _*_ coding: utf-8 _*_


from flask import Blueprint, render_template
from flask_login import login_required

from bluelog.forms import SettingForm

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingForm()
    return render_template('admin/settings.html', form=form)
