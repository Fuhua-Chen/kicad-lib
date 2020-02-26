#!/usr/bin/python
#coding:utf-8
import os

# init and update git module
os.system('git submodule init')
os.system('git submodule update')
# install some module
os.system('pip install pandas')