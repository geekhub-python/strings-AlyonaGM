#!/usr/bin/env python3

print("Введите данные: ")

s = input()
e = s[0:int(((len(s)/2) + len(s) % 2))]
f = s[int(((len(s)/2) + len(s) % 2)):]
print(f + e)
