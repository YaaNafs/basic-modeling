# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 17:59:48 2022

@author: hp
"""
file = open("test.txt")
bad_dict = {():6}
print(() in bad_dict)

listk = ["rs"]
print("rs" in listk)

txt = {4:"1",2:3,3:6,9:"2"}
print(txt[4]+"{x} {y}".format(y=3,x="4"))
for x in enumerate(txt[4]):
    print(x)

ct=0
for l in file:
    ct += l.count("e")
print(f"{ct}")

numlist = [2,5,5,0,9,3,2,5]
def addsquare(listitems):
    num = listitems[0]
    if len(listitems) == 1:
        return num**2
    listitems.remove(num)
    return num**2 + addsquare(listitems)
print("Total: {}".format(addsquare(numlist)))