#!/usr/bin/python
# coding:utf-8

"""术语归类
@author: yyhaker
@contact: 572176750@qq.com
@file: term_classification.py
@time: 2019/4/29 20:59
"""
# def term_classification(terms):
#     """直接暴力.
#     :param terms:
#     :return:
#     ----
#     时间复杂度O(n^2), 空间复杂度O(n)
#     """
#     res = []
#     for t in terms:
#         cur = set(t)
#         flag = False  # 表示与之前的术语对有没有交集
#         for i, item in enumerate(res):
#             if cur & item:
#                 flag = True
#                 item = cur | item
#                 res[i] = item
#                 break
#         if not flag:
#             res.append(cur)
#     return res

def term_classify_set(terms):
    """使用并查集求解术语归类问题.
    -----
    时间复杂度为O(n)，空间复杂度为O(n)
    :param terms:
    :return:
    """
    # make set
    parent = {}
    for term in terms:
        x, y = term
        parent[x] = x
        parent[y] = y
    # union set
    for term in terms:
        x, y = term
        px = find_set(x, parent)
        py = find_set(y, parent)
        if px != py:
            parent[py] = px
    # 输出归类
    ps = {}
    for item in parent.keys():
        p = find_set(item, parent)
        if p not in ps:
            ps[p] = []
        ps[p].append(item)
    for v in ps.values():
        print(" ".join(v))
    return ps

def find_set(x, parent):
    """找到x的根"""
    if parent[x] == x:
        return x
    # 将该路径上的所有点都指向根节点
    parent[x] = find_set(parent[x], parent)
    return parent[x]


if __name__ == "__main__":
    terms = [
        ("苹果", "梨"),
        ("汽车", "火车"),
        ("北京", "南京"),
        ("苹果", "香蕉"),
        ("上海", "南京")
    ]
    term_classify_set(terms)
