#
import os, sys

__all__ = [
    "Config",
    ]

My_Module_Name = "custom_config"

if not 'My_Module_Path' in globals():
    if '__path__' in globals():
        My_Module_Path = __path__
    else:
        My_Module_Path = os.getcwd()

from ._custom_config import Config

Config_Dir = os.getenv( 'CUSTOM_CONFIG_DIR', default=os.getcwd() )

if not 'Default_ConfigFile' in globals():
    Default_ConfigFile = os.getenv( 'CUSTOM_CONFIG_FILE', default=My_Module_Name + '.conf' )

if not 'Default_Config' in globals():
    Default_Config = {}

del os, sys
