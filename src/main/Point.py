#!/usr/bin/python
# _*_ coding: UTF-8 _*_

class Point:
    def __init__(self, x=0, y=0):
        self.x = x;
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "销毁"


pt1 = Point()
pt2 = pt1
pt3 = pt1



