#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: leftTreeSum.py
@time: 2019/3/19 21:01
"""
# 建立一棵树
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build_tree(pre=[3, 1, 2, 4, 6], ins=[1, 3, 4, 2, 6]):
    """
    根据前序遍历和后续遍历建立一棵数.
    :param pre:
    :param ins:
    :return:
    """
    if len(pre) == 0 or len(ins) == 0:
        return None
    if len(pre) == 1:
        return TreeNode(pre[0])
    else:
        root = TreeNode(pre[0])
        root.left = build_tree(pre[1: 1+ins.index(pre[0])], ins[0: ins.index(pre[0])])
        root.right = build_tree(pre[1+ins.index(pre[0]):], ins[ins.index(pre[0])+1:])
    return root

def pre_order(root):
    """先序遍历"""
    if root:
        print(root.val)
        pre_order(root.left)
        pre_order(root.right)

def ins_order(root):
    if root:
        ins_order(root.left)
        print(root.val)
        ins_order(root.right)

def getLeftLeafSum(root):
    """
    求一个树的所有左叶子结点的和.
    :param root:
    :return:
    """
    if root is None:
        return 0
    else:
        sum = 0
        # 如果当前结点的左结点是叶子结点，那么就加上去
        if root.left and root.left.left is None and root.left.right is None:
            sum += root.left.val
        return sum + getLeftLeafSum(root.left) + getLeftLeafSum(root.right)

root = build_tree()
# pre_order(root)
# print("*"*200)
# ins_order(root)
sum = getLeftLeafSum(root)
print(sum)


root = build_tree(pre=[3, 1, 4, 5, 3, 6], ins=[1, 3, 3, 5, 4, 6])
# pre_order(root)
# print("*"*200)
# ins_order(root)
sum = getLeftLeafSum(root)
print(sum)

