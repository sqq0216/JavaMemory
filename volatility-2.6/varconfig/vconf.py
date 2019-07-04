#-*-coding:utf-8-*-
import ConfigParser
import os

curpath = os.path.dirname(os.path.realpath(__file__))
cfgpath = os.path.join(curpath, "varcfg.ini")


conf = ConfigParser.ConfigParser()
conf.read(cfgpath)
sections = conf.sections()

# items = conf.items('section')
# print items

hostname = conf.get("ssh", "hostname")
port = conf.get("ssh", "port")
username = conf.get("ssh", "username")
password = conf.get("ssh", "password")
