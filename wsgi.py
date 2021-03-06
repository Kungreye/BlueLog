#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


from bluelog import create_app

app = create_app('production')