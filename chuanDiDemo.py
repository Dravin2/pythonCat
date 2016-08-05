#!/usr/bin/env python
#-*- coding:utf-8 -*-

#===值传递
a = 1

def change_integer(a):
        a = a + 1
        return a

print change_integer(a)      #注意观察结果
print a      #注意观察结果

#===指针传递
b = [1,2,3]

def change_list(b):
    b[0] = b[0] + 1
    return b

print change_list(b)      #注意观察结果
print b      #注意观察结果
