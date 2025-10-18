"""
Given two integers a and b, return any string s such that:

s has length a + b and contains exactly a 'a' letters, and exactly b 'b' letters,
The substring 'aaa' does not occur in s, and
The substring 'bbb' does not occur in s.
 

Example 1:

Input: a = 1, b = 2
Output: "abb"
Explanation: "abb", "bab" and "bba" are all correct answers.
Example 2:

Input: a = 4, b = 1
Output: "aabaa"
"""


def strWithout3a3b(a: int, b: int) -> str:
    
    count_a = 0
    count_b = 0

    result = ""

    for i in range(a+b):
        if a !=0 and count_a <2 and (count_b ==2 or a>=b):
            result += "a"
            a -= 1
            count_a += 1
            count_b = 0
        elif b !=0 and count_b <2 and (count_a ==2 or b>=a):
            result += "b"
            b -= 1
            count_b += 1
            count_a = 0 

    return result


if __name__ == "__main__":
    a = 1
    b = 2
    res = strWithout3a3b(a, b)
    print(res)