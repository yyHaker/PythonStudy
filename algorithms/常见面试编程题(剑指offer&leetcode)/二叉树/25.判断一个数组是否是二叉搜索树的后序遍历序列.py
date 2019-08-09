#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 判断一个数组是否是二叉搜索树的后序遍历序列.py
@time: 2019/7/11 20:09
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        # 思路：（1）判断输入为空、二叉树只有左子树、二叉树只有右子树的情况
        #       (2) 使用index分割左右子树，递归判断左右子树是否为后续遍历序列
        if len(sequence) == 0:
            return False
        root = sequence[-1]
        # 二叉树只有一个子树的情况下是后续遍历
        if max(sequence) < root or min(sequence) > root:
            return True

        # 找到划分左右子树的index
        index = 0
        length = len(sequence)
        for i in range(length - 1):
            index = i
            if sequence[i] > root:
                break
        for j in range(index + 1, length - 1):
            if sequence[j] < root:
                return False
        left = True
        right = True
        # 是否存在左子树
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[0: index])
        # 是否存在右子树
        if index < length - 1:
            right = self.VerifySquenceOfBST(sequence[index: length - 1])
        return left and right
