import os
from configparser import SafeConfigParser

env = os.environ.get('ENV', 'dev')
config = SafeConfigParser()
config.read('config_files/{}_config.ini'.format(env))
