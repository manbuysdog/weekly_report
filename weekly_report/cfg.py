import os
from configparser import SafeConfigParser

config = SafeConfigParser()
config.read('config_files/{}_config.ini'.format(os.environ.get('env','dev')))
