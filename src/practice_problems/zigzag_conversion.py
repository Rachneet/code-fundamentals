"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""

def convert(s: str, numRows: int) -> str:
        
    n = len(s)
    result = [""] * numRows

    if numRows == 1 or numRows == n:
        return s

    backward = True
    index = 0
    for char in s:
        result[index] += char
        if index == 0 or index == numRows - 1:
            backward = not backward

        if backward:
            index -= 1
        else:
            index += 1
    
    return "".join(result)


if __name__ == "__main__":
    s = "PAYPALISHIRING"
    numRows = 3

    res = convert(
        s=s,
        numRows=numRows
    )
    print(res)

