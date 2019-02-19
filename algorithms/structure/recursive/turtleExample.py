#!/usr/bin/python
# coding:utf-8

"""
@author: yyhaker
@contact: 572176750@qq.com
@file: turtleExample.py
@time: 2019/2/19 11:42
"""
import turtle

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle, lineLen-5)


def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        t.backward(branchLen)


def example1():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    drawSpiral(myTurtle, 100)
    myWin.exitonclick()

def example2():
    myTurtle = turtle.Turtle()
    myWin = turtle.Screen()
    myTurtle.left(90)
    myTurtle.up()
    myTurtle.backward(100)
    myTurtle.down()
    myTurtle.color("green")
    tree(75, myTurtle)
    myWin.exitonclick()


if __name__ == "__main__":
    example2()

