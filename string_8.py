#!/usr/bin/env python3

a = input()
b = a.find('f')
c = str(b)
d = a.rfind('f',b + 1)
s =str(d)
print(c.replace('-1', ''), s.replace('-1', ''))