"""
Given an array of strings words and a width maxWidth, format the text 
such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line does not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
 

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified 
instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""

from typing import List


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    result = []
    current_line = []
    current_length = 0
    
    for word in words:
        # Check if adding this word exceeds maxWidth
        # current_length + len(current_line) accounts for minimum spaces between words
        if current_length + len(current_line) + len(word) > maxWidth:
            # Justify and add current line
            result.append(justify_line(current_line, maxWidth, False))
            current_line = []
            current_length = 0
        
        current_line.append(word)
        current_length += len(word)
    
    # Last line - left align
    result.append(justify_line(current_line, maxWidth, True))
    return result


def justify_line(words, maxWidth, is_last):
    if is_last or len(words) == 1:
        # Left align: join with single spaces, pad right
        line = ' '.join(words)
        return line + ' ' * (maxWidth - len(line))
    
    # Full justify
    total_chars = sum(len(word) for word in words)
    total_spaces = maxWidth - total_chars
    gaps = len(words) - 1
    
    # Distribute spaces evenly
    spaces_per_gap = total_spaces // gaps
    extra_spaces = total_spaces % gaps  # Leftover spaces go to left gaps
    
    line = ""
    for i, word in enumerate(words):
        line += word
        if i < gaps:  # Not the last word
            # Add base spaces + 1 extra if this gap gets a leftover
            line += ' ' * (spaces_per_gap + (1 if i < extra_spaces else 0))
    
    return line


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16

    res = fullJustify(
        words=words,
        maxWidth=maxWidth
    )

    print(res)