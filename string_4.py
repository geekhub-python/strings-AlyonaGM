#!/usr/bin/env python3

print("Введите данные: ")

s = input()
print("Выходне данные")
print(s[s.find(' ') + 1:] + " " + s[:s.find(' ') + 1])
