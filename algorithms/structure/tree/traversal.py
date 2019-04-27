#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: search.py
@time: 2019/2/21 11:26
"""
# 树的遍历

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def inorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        print(tree.getRootVal())
        preorder(tree.getRightChild())

def postorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        print(tree.getRootVal())