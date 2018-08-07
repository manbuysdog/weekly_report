import os
from configparser import SafeConfigParser

def load_config(env):
    """
    
    """
    print("loading config for {}".format(env))
    config = SafeConfigParser()
    location = './weekly_report/config_files/{}_config.ini'.format(env)
    config.read(os.path.abspath(location))
    return config
