#!/usr/bin/python
# -*- coding: UTF-8 -*-

class JustCounter:
    __privateCount = 0
    publicCount = 0

    def count(selfs):
        selfs.__privateCount += 1
        selfs.publicCount += 1
        print selfs.__privateCount


counter = JustCounter()
counter.count()
print counter.publicCount
# print counter.__privateCount
print counter._JustCounter__privateCount
