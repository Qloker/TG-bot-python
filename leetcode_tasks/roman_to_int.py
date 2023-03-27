'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

s = "III"

ans = []
a = 0

for i in s:
    if i == "I":
        a += I
    if i == "V":
        a += V
    if i == "X":
        a += X
    if i == "L":
        a += L
    if i == "C":
        a += C
    if i == "D":
        a += D
    if i == "M":
        a += M   

if 'CD' in s:
    a -= 200
    print(a)
if 'CM' in s:
    a -= 200
    print(a)
if 'XL' in s:
    a -= 20
    print(a)
if 'XC' in s:
    a -= 20
    print(a)
if 'IV' in s:
    a -= 2 
    print(a)
if 'IX' in s:
    a -= 2
    print(a)
print(a)

'''
if "I" in s:
    a += I
    print(a)
if 'V' in s:
    a += V
    print(a)
if 'X' in s:
    a += X
    print(a)
if 'L' in s:
    a += L
    print(a)
if 'C' in s:
    a += C
    print(a)
if 'D' in s:
    a += D
    print(a)
if 'M' in s:
    a += M
    print(a)

for i in range(0, len(s), 2):
    print(a)
    if i == 'CD':
        a -= 200
        print(a)
    if i == 'CM':
        a -= 200
        print(a)
    if i == "XL":
        a -= 20
        print(a)
    if i == 'XC':
        a -= 20
        print(a)
    if i == 'IV':
        a -= 20
        print(a)
    if i == 'IX':
        a -= 20
        print(a)
'''
