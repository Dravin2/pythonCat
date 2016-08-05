#!/usr/bin/env python3
# -*-coding:utf-8 -*-

print("hello")

a=10
b=1.3
c="hello"
d=True

print type(a)
print type(b)
print type(c)
print type(d)


print("tuple的各个元素不可再变更，而list的各个元素可以再变更")
tuple1=(a,b,c,d)
print tuple1,type(tuple1)

list1=[a,b,c,d]
print list1,type(list1)


list2=[1,[3,4,5]]
list3=[]

print tuple1[0]
print list1[2]
print list2[1][2]

list1[1]=3.0
print list1


s1=(2, 1.3, 'love', 5.6, 9, 12, False)
s2 = [True, 5, 'smile']
s3 = [1,[3,4,5]]
s4 = []

print "s1:",s1
print "0<=x<5",s1[:5]
print "2<=x",s1[2:]
print "[2,5) x+=2",s1[2:5:2]
print "[2,0) x-=1",s1[2:0:-1]

print s1[-1]
print s1[-3]




#---string

str="abcdefg"

print str[2:4]

print 5 in [1,3,5]


