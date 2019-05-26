#!/usr/bin/python
# coding:utf-8

"""二叉搜索树(BST)
@author: yyhaker
@contact: 572176750@qq.com
@file: binarySearchTree.py
@time: 2019/5/25 15:00
"""
import random

class BinarySearchTree(object):
    """Binary Search Tree with n nodes."""
    def __init__(self):
        # 根结点
        self.root = None

    def in_order_walk(self, x):
        """
        中序遍历, 时间复杂度为O(n)
        :param x: 结点x
        :return:
        """
        if x != None:
            self.in_order_walk(x.left)
            print(x.key)
            self.in_order_walk(x.right)

    def search(self, x, k):
        """查找关键字等于k的结点，时间复杂度为O(h)
        :param x: 结点x
        :param k: 关键字
        :return:
        """
        while x != None and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def minimum(self, x):
        """查找最小关键字元素
        :param x:
        :return:
        """
        while x.left != None:
            x = x.left
        return x

    def maxmum(self, x):
        """查找最大关键字元素
        :param x:
        :return:
        """
        while x.right != None:
            x = x.right
        return x

    def successor(self, x):
        """
        得到一个节点x的后继节点, 时间复杂度O(h)
        :param x:
        :return: if none means no successor.
        """
        # x的右子树不为空，则x的后继为x的右子树中具有最小关键字的结点
        if x.right != None:
            return self.minimum(x.right)
        else:
            # x的右子树为空， 则x的后继y为x的最底层祖先，而且y的右孩子要么是结点x本身，要么也是x的一个祖先
            y = x.p
            while y != None and x == y.right:
                x = y
                y = y.p
            return y

    def predecessor(self, x):
        """
        得到一个节点的前驱，时间复杂度为O(h)
        :param x:节点x
        :return: if none means no predecessor
        """
        # x的左子树不为空，则x前驱为x的左子树中具有最大关键字的结点
        if x.left != None:
            return self.maxmum(x.left)
        else:
            # x的左子树为空，  则x的前驱y为x的最底层祖先，而且y的左孩子要么是结点x本身，要么也是x的一个祖先
            y = x.p
            while y != None and x == y.left:
                x = y
                y = y.p
            return y

    def insert(self, z):
        """
        插入一个节点z.
        :param z:
        :return:
        """
        # 如果树为空，直接作为根结点
        if self.root == None:
            self.root = z
        else:
            y = None
            x = self.root
            # 寻求树中z的合适位置
            while x != None:
                y = x
                if z.key < x.key:
                    x = x.left
                else:
                    x = x.right
            # 将结点z插入到该位置
            z.p = y
            if z.key < y.key:
                y.left = z
            else:
                y.right = z

    def delete(self, z):
        """
        删除一个节点z
        :param z:
        :return:
        """
        # 如果z最多有一个孩子节点
        if z.left == None:
            self._transplant(z, z.right)
        elif z.right == None:
            self._transplant(z, z.left)
        # 如果z两个节点都存在，则寻找其后继，即z的右子树的最小值
        else:
            y = self.minimum(z.right)  # 后继节点
            if y.p != z:     # 如果z的后继结点y不是z的右孩子
                self._transplant(y, y.right)  # 用y的右孩子代替y
                y.right = z.right
                y.right.p = y    # 直接将y的右孩子(原来z的右孩子)的父结点设为y
            self._transplant(z, y)  # 直接用z的后继y代替z
            y.left = z.left
            y.left.p = y

    def _transplant(self, u, v):
        """
        二叉树内移动子树，用子树v替换子树u并成为u的双亲的孩子结点
        :param u:
        :param v:
        :return:
        """
        # v替换u
        if u.p == None:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p


class Node(object):
    """Node object"""
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None
        self.p = None


if __name__ == "__main__":
    print("生成二叉树结点并插入树中: ")
    nodes = [Node(random.randint(1, 100)) for i in range(10)]
    # numbers = [14, 25, 30, 32, 44, 51, 75, 78, 89, 92]
    # nodes = [Node(i) for i in numbers]
    bst = BinarySearchTree()
    for node in nodes:
        print("insert node: ", node.key)
        bst.insert(node)

    print("中序遍历： ")
    bst.in_order_walk(bst.root)

    print("查找指定的结点: {}".format(nodes[3].key))
    res = bst.search(bst.root, k=nodes[3].key)
    print("查找结果: ")
    print("自身关键字: {},  父结点的关键字: {}".format(res.key, res.p.key))

    minimum = bst.minimum(bst.root)
    print("树中最小关键字: ", minimum.key)

    maximum = bst.maxmum(bst.root)
    print("树中最大关键字：", maximum.key)

    x = bst.predecessor(nodes[3])
    if x != None:
        print("结点{}的前驱: {}".format(nodes[3].key, x.key))
    else:
        print("结点{}没有前驱".format(nodes[3].key))

    x = bst.successor(nodes[3])
    if x != None:
        print("结点{}的后继: {}".format(nodes[3].key, x.key))
    else:
        print("结点{}没有后继".format(nodes[3].key))
    print("删除结点{}, 并中序输出查看结果: ".format(nodes[3].key))
    bst.delete(nodes[3])
    bst.in_order_walk(bst.root)



