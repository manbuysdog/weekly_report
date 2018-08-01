import weekly_report.cfg
import unittest
import os
#from weekly_report.cfg import load_config

class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_simple(self):
        self.assertTrue(1 == 1)

    def test_load_config(self):
        #conf = load_config('test')
        self.assertTrue(conf.get('env', 'name') == 'test')
