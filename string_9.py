#!/usr/bin/env python3

s = input()
a = s.count('f')
if a < 1:
    print(-2)
elif a == 1:
    print(-1)
else:
    print(s.find('f',s.find('f') + 1))