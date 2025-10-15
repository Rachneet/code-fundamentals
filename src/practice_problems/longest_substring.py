"""
Given a string s having lowercase characters, find the length of the 
longest substring without repeating characters. 

Examples:

Input: s = "geeksforgeeks"
Output: 7 
Explanation: The longest substrings without repeating characters are "eksforg” and "ksforge", with lengths of 7.

Input: s = "aaa"
Output: 1
Explanation: The longest substring without repeating characters is "a"

Input: s = "abcdefabcbb"
Output: 6
Explanation: The longest substring without repeating characters is "abcdef".
"""


def longest_unique_substring(s: str):
    """
    naive approach
    """

    res = 0

    for i in range(len(s)):
        sub_list = [s[i]]
        for j in range(i+1, len(s)):
            if s[j] not in sub_list:
                sub_list.append(s[j])
            else:
                break
        
        res = max(res, len(sub_list))

    return res



if __name__ == "__main__":
    s = "geeksforgeeks"
    res = longest_unique_substring(s)
    print(res)
