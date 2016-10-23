#!/usr/bin/env python3

s = input()
t = s.find("h")
v = s.rfind("h")
print(s[:t] + s[v+1:])