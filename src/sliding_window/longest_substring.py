"""
Given a string s, find the length of the longest substring without duplicate characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(s: str) -> int:
    
    left = 0
    n = len(s)

    result = 0
    sub_str = ""

    for right in range(n):

        while s[right] in sub_str:
            result = max(result, len(sub_str))
            sub_str = sub_str[left+1:]
            left += 1

        sub_str += s[right]
        print(len(sub_str))

    return result






if __name__ == "__main__":
    s = "abcabcbb"
    s = "   "
    res = lengthOfLongestSubstring(s)
    print(res)
