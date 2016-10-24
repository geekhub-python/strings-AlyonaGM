#!/usr/bin/env python3

s = input()
t = s.find("h")
v = s.rfind("h")
w = s[t+1:v]
print(s[:t+1] + w[::-1] + s[v:])