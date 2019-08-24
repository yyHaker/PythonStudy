#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: 31.二叉搜索树中的中序后继结点.py
@time: 2019/8/23 11:14
"""
"""
leetcode285： 二叉搜索树中的中序后继结点
思路：利用二叉搜索树的性质, 比p节点大的在它的右边, 我们只需找到比p节点值大的最小节点. 
先将结果初始化为None, 如果p的值小于root, 那么我们更新结果为root, 然后往左边搜索, 
当往右边搜索时, 我们不用更新结果, 因为要么之前已找到更小的结果, 要么还没找到比p节点的值更大的节点.
Time: O(h), h为树的高度
Space: O(1)
"""
class Solution(object):
    def inorderSuccessor(self, root, p):
        ans = None
        while root:
            if p.val < root.val:
                ans = root
                root = root.left
            else:
                root = root.right
        return ans


