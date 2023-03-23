import sqlite3

import requests
import json
import random

l1 = ['s', 'c', 'a', 'a', 'a', 'a', 'a']
l1.remove('s')
print(l1)

if 'a' in l1:
    l1.remove('a')
    print('a - deleted')
    print(l1)
else:
    print('did not contain')

count = l1.count('a')

if count > 0:
    for i in range(count):
        l1.remove('a')
    print(l1)
else:
    print('did not have')