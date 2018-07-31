import os
from configparser import SafeConfigParser

config = load_config('dev')

def load_config(env):
    config = SafeConfigParser()
    config.read('config_files/{}_config.ini'.format(env))
    return config