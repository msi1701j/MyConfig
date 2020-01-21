#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys, os
import six

sys.path.append(os.getenv('MY_MODULE_PATH', default=os.getcwd()))
from custom_config import Config


class TestConfig(unittest.TestCase):
    def setUp(self):
        self.config = Config( "sample.conf" )

    def tearDown(self):
        del self.config
        
    def test_0010_init(self):
        """ test __init__() and __getitem__() """
        self.assertEqual( self.config['test1'] , "local test1 message", "Should be 'local test1 message'" )

    def test_0020_test2(self):
        """ test __getitem__(), test2 message is added by local """
        self.assertEqual( self.config['test2'] , "local test2 message", "Should be 'local test2 message'" )

    def test_0030_test3(self):
        """ test __getitem__(), test3 message remains in default """
        self.assertEqual( self.config['test3'] , "defaults test3 message", "Should be 'defaults test3 message'" )

    def test_0040_add(self):
        """ test __setitem__() and __delitem__() """
        test2_msg = "test2 message"
        self.config['test2'] = test2_msg
        self.assertEqual( self.config['test2'], test2_msg, "Should be 'test2 message'" )
        del self.config['test2']

    def test_0050_contains(self):
        """ test __contains__() """
        self.assertTrue( "test1" in self.config, "config should contains 'test1'" )

    def test_0060_iter(self):
        """ test __iter__() """
        i = 0
        for k in self.config:
            i = i + 1
        self.assertEqual( i, 4, "Should be 4" )

    def test_0060_delitem(self):
        """ test __delitem__() """
        del self.config['test3']
        self.assertFalse( "test3" in self.config, "config should not contains 'test3'" )

    def test_0070_delitem2(self):
        """ test __delitem__(), which key does not exist in config and delete it with no error"""
        self.assertFalse( "test5" in self.config, "config should not contains 'test5'" )
        del self.config['test5']
        self.assertFalse( "test5" in self.config, "config should not contains 'test5'" )

    
if __name__ == "__main__":
    unittest.main()
