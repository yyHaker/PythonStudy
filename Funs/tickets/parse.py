# -*- coding: utf-8 -*-
import re
from pprint import pprint

with open("station_name.html", 'r', encoding="utf-8") as f:
    text = f.read()
    # 提取出中文名和大写字母的代号信息
    stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', text)
    pprint(dict(stations), indent=4)
