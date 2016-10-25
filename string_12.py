#!/usr/bin/env python3

a = input()
print(*(a[i] for i in range(len(a)) if i%3), sep='')