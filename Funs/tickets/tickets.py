# -*- coding: utf-8
"""Train tickets query via command-line

Usage:
      tickets [-gdtkz] <from> <to> <date>

Options:
      -h, --help  显示帮助菜单
      -g             高铁
      -d             动车
      -t             特快
      -k             快速
      -z             直达

Example:
    tickets 南京 北京 2016-07-01
    tickets -dg 南京 北京 2016-07-01
"""
import argparse
from docopt import docopt
from stations import stations
import requests
from prettytable import PrettyTable

def cli():
    """command-line interface"""
    parse = argparse.ArgumentParser(description="Train tickets query via command-line")
    parse.add_argument("-g", action="store", dest="g", help="高铁")
    parse.add_argument("-d", action="store", dest="d", help="动车")
    parse.add_argument("-t", action="store", dest="t", help="特快")
    parse.add_argument("-k", action="store", dest="k", help="快速")
    parse.add_argument("-z", action="store", dest="z", help="直达")
    parse.add_argument("-from", action="store", dest="from_station",default=u"深圳", help="出发站")
    parse.add_argument("-to", action="store", dest="to_station", default=u"北京", help="到达站")
    parse.add_argument("-date", action="store", default="2018-02-09", help="出发日期")
    print(parse.parse_args())
    params = parse.parse_args()
    from_station = stations.get(params.from_station)
    to_station = stations.get(params.to_station)
    date = params.date
    # 构建URL
    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=={}' \
          '&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.\
        format(date, from_station, to_station)
    
    # 使用request请求URL
    r = requests.get(url, verify=False)
    print("The request URL is "+url)
    print(r.status_code)
    r.encoding = "ISO"
    print(r.text)

    # 使用prettyTable显示得到的json数据
    headers = '车次 车站 时间 历时 商务 一等 二等 软卧 硬卧 软座 硬座 无座'.split()
    pt = PrettyTable()
    pt._set_field_names(headers)
    print(pt)


if __name__ == "__main__":
    cli()
# TODO: 能否使用python request模拟浏览器的请求响应行为？
