# -*- coding: utf-8 -*-
"""

"""

from PIL import Image
import sys

import pyocr
import pyocr.builders

import os

user_name = os.environ['USERPROFILE'].replace('\\', '/')

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))
lang = langs
print("Will use lang '%s'" % (lang))

input_file = user_name + '/Desktop/ocr.jpg'

txt = tool.image_to_string(
    Image.open(input_file),
    lang='jpn',
    builder=pyocr.builders.TextBuilder()
)
txt = txt.replace(' ', '')

ocr_img = '\n'.join(filter(lambda x: x.strip(), txt.split('\n')))

with open(user_name + '/Desktop/ocr_img.txt', mode='w')as f:
    f.write(ocr_img)
