'''
Given an integer x, return true if x is a 
palindrome
, and false otherwise.

 
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
'''
class Solution(object):
    def isPalindrome(x):

        list_of_num = []
        new_list = []

        for i in range(0, len(str(x))):
            list_of_num.append(str(x)[i])

        for i in range(len(str(x)) - 1, -1, -1):
            new_list.append(str(x)[i])

        if list_of_num == new_list:
            return True
        else:
            return False

        """
        :type x: int
        :rtype: bool
        """
test = Solution
test.isPalindrome(141)


n = 414

list_of_number = []
new_list = []
str_of_number = str(n)

for i in range(0, len(str_of_number)):
    list_of_number.append(str_of_number[i])

print(list_of_number, len(list_of_number))


# range(10, 0, -1), ДЛЯ ОБРАТНОЙ ПОСЛЕДОВАТЕЛЬНОСТИ НЕОБХОДИМО ЗАДАТЬ ШАГ

for i in range(len(list_of_number) - 1, -1, -1):
    new_list.append(str_of_number[i])

if new_list == list_of_number:
    print('Palindrome')
else: 
    print('not a pal')
