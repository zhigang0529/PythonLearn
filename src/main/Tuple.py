#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'czg'
from collections import namedtuple

# 拆包

tuple_1 = ("Jack1", 30, 188.1)
tuple_1 = ("Jack", 20, 170.1)
name, age, height = tuple_1
print("name: %s, age: %d, height: %d" % (name, age, height))

# namedtuple
User = namedtuple("User", ["name", "age", "height", "sex"])
user = User(name="Joe", age=29, height=180.0, sex="female")
print(user.name, user.age, user.height)

user_tuple = ("Tom", 33, 190, "male")
user2 = User(*user_tuple)
print(user2.name, user2.age, user2.height, user2.sex)
