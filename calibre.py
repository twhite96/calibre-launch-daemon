#!/usr/bin/env python3

import os

path = "/Applications/calibre.app"
flags = os.O_RDONLY
mode = 0o666
os.open(path, flags, mode)
