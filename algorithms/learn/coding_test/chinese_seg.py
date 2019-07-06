#!/usr/bin/python
# coding:utf-8

"""中文分词
@author: yyhaker
@contact: 572176750@qq.com
@file: chinese_seg.py
@time: 2019/4/29 22:16
"""
def forward_max_match(vocabs, sent, max_len=3):
    """正向最大匹配.
    :param vocabs: 词表
    :param sent: string, 句子
    :return:
    """
    res = []
    line = list(sent)
    while len(line) > 0:
        try_word = line[0: max_len]
        while "".join(try_word) not in vocabs:
            if len(try_word) == 1:
                break
            try_word = try_word[0: len(try_word)-1]
        res.append("".join(try_word))
        line = line[len(try_word):]
    return " ".join(res)

def backward_max_match(vocabs, sent, max_len=3):
    """
    逆向最大匹配
    :param vocabs:
    :param sent:
    :param max_len:
    :return:
    """
    res = []
    line = list(sent)
    while len(line) > 0:
        try_word = line[-max_len:]
        while "".join(try_word) not in vocabs:
            if len(try_word) == 1:
                break
            try_word = try_word[1:]
        res.insert(0, "".join(try_word))
        line = line[0: len(line) - len(try_word)]
    return " ".join(res)


if __name__ == "__main__":
    vocabs = ["我", "爱", "北京", "天安门"]
    sent = "我爱北京天安门。"
    res = forward_max_match(vocabs, sent)
    # res = backward_max_match(vocabs, sent)
    print(res)