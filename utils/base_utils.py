# coding=utf-8
import os
import configparser

root_path=os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

def get_config_value(section,key):
    conf_path=os.path.join(root_path,"config","config.ini")
    conf=configparser.ConfigParser()
    conf.read(conf_path,encoding='utf-8')
    value=conf.get(section,key)
    return value
