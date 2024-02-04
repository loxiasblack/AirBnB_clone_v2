#!/usr/bin/python3

import importlib
from fabric.api import env

pack_module = importlib.import_module("1-pack_web_static")
do_pack = pack_module.do_pack
depl
