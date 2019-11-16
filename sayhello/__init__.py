# -*- coding: utf-8 -*-
"""
    :author: Grey Li (李辉)
    :url: http://greyli.com
    :copyright: © 2018 Grey Li <withlihui@gmail.com>
    :license: MIT, see LICENSE for more details.
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# 所增加的拓展功能
db = SQLAlchemy(app)
# bootstrap没有被用到后端, 而是被用到了前端，但是是怎么被传到前端的呢？
bootstrap = Bootstrap(app)
moment = Moment(app)

from sayhello import views, errors, commands
