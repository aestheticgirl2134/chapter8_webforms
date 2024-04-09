import os

class Config(object):
    """define app configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY')or 'hard-to-guess'