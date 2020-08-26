# -*- coding=utf-8 -*-

import os
import click

from flask import Flask,render_template
from blueblog import create_app
from settings import config

app=create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.route('/')
def hello_world():
    secret_key=os.getenv('SECRET_KEY','new blue blog')
    server=os.getenv('MAIL_SERVER')
    file_name=__file__
    flag='test none'
    if file_name is None:
        flag='none'
    body='<p>'+secret_key+'</p></br>'+'<p>'+file_name+'</p>'+flag+server
    return body

@app.cli.command()
def test():
    """Run the unit tests."""
    import unittest
    tests=unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

