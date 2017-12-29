# -*- coding: utf-8 -*-  
from distutils.core import setup
import py2exe
import sys
 
#this allows to run it with a simple double click.
sys.argv.append('py2exe')
 
py2exe_options = {
        "includes": ["sip"],
        "dll_excludes": ["MSVCP90.dll",],
        "compressed": 1,
        "optimize": 2,
        "ascii": 0,
        #"bundle_files": 1,
        }
 
setup(
      name = '桥梁避碰终端配置工具',
      version = '1.0',
      #windows = ['gis_serial.py',],
      zipfile = None,
      options = {'py2exe': py2exe_options},
      windows = [{"script": "win.py",  
            "icon_resources": [(1, u"./img/image1.ico")]  
           }]  
      )
