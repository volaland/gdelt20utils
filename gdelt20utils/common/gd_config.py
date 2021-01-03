import os
from configparser import SafeConfigParser

config = SafeConfigParser(os.environ)
config.read("config.ini")
