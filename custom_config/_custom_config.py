#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/opt/splunk/bin/python
"""
a module for reading config file
at this time, supporting [defaults] seciton only
"""

import sys, os, io
import logging

import six
if six.PY2:
    import ConfigParser as configparser
else:
    import configparser

if not 'My_Module_Name' in globals():
    My_Module_Name = "custom_config"

if not 'My_Module_Path' in globals():
    if '__path__' in globals():
        My_Module_Path = __path__
    else:
        My_Module_Path = os.getcwd()

Config_Dir = os.getenv( 'CUSTOM_CONFIG_DIR', default=os.getcwd() )
    
if not 'Default_ConfigFile' in globals():
    Default_ConfigFile = os.getenv( 'CUSTOM_CONFIG_FILE', default=My_Module_Name + '.conf' )

if not 'Default_Config' in globals():
    Default_Config = {}

class Config:
    global Default_ConfigFile
    global Default_Config
    global Config_Dir

    def __init__(self, config_file=Default_ConfigFile, default_config=Default_Config):
        """ Constructor for Config class """
        self.__configfile = config_file
        self.__config = self.__load_config( self.__configfile )

        self.__params = {}
        for key in default_config:
            lkey = key.lower()
            self.__params[lkey] = default_config[key]

        default_section = []
        if 'defaults' in self.__config.sections():
            default_section = self.__config.items('defaults')
        for key, value in default_section:
            lkey = key.lower()
            self.__params[lkey] = value

    def __getitem__(self, key):
        """ operator '=' to get item """
        lkey = key.lower()
        if lkey in self.__params:
            return self.__params[lkey]
        return None

    def __setitem__(self, key, value):
        """ operator '=' to set item """
        self.__params[key.lower()] = value

    def __delitem__(self, key):
        del self.__params[key.lower()]

    def __contains__(self, key):
        """ operator 'in' as a boolean to test item in this class """
        return key.lower() in self.__params

    def __iter__(self):
        """ for iterator operation """
        for key in self.__params:
            yield key

    # app_root()
    # App のルートディレクトリ
    def __app_root(self):
        """ get the application root """
        # app_file = getattr(sys.modules['__main__'], '__file__', sys.executable)
        # # return os.path.dirname(os.path.abspath(os.path.dirname(app_file)))
        # return os.path.abspath(os.path.dirname(app_file))
        return os.path.abspath(Config_Dir)


    # _search_path()
    # 独自の conf ファイルの検索パスの生成
    def __search_path(self, name, candidate_dirs=['default', 'local']):
        """ get search path for config file """
        self.__root = self.__app_root()
        paths = [p for p in [os.path.join(self.__root, d, name) for d in candidate_dirs] if os.path.exists(p)]
        return paths


    # load_config()
    # 見つかった候補ディレクトリから、設定ファイルを読出し、 ConfigParser で読込みます。
    def __load_config(self, name, candidate_dirs=['default', 'local'], encoding='utf_8_sig'):
        """ load config file """
        config = configparser.ConfigParser()
        for cf in self.__search_path(name, candidate_dirs):
            with io.open(cf, encoding=encoding) as f:
                if six.PY2:
                    config.readfp(f)
                else:
                    config.read_file(f)
                logging.info("%s has been loaded", cf)
        return config


def main():
    six.print_( 'in main' )
    config = Config(My_Module_Name + '.conf')
    six.print_(config)
    for key in config:
        six.print_( key + ': ' + config[key] )

if __name__ == '__main__':
    main()

