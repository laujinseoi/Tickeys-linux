#! /usr/bin/env python
#-----------------------------------------------------------------------------
# Copyright (c) 2013, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License with exception
# for distributing bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

# from  PyInstaller import  *


# I try to use this thing to package, but fail.
__author__ = 'Huang xiongbiao(billo@qq.com)'
import  os

if __name__ == '__main__':
    from PyInstaller.main import run
    opts=['CLI.py']
    run(opts)