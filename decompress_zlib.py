#!/usr/bin/env python

import zlib

filename = 'coin_text_base64_decoded.txt'
data = open(filename).read()

zlib.decompress(data)
