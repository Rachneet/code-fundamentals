def reverse_string(s: str) -> str:
    """Return the reverse of the input string.

    Args:
        s (str): The string to be reversed.

    Returns:
        str: The reversed string.

    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("Python")
        'nohtyP'
        >>> reverse_string("")
        ''
    """
    return s[::-1]


def reverse_string_v2(s: str):

    """
    two pointer solution
    """
    
    left, right = 0, len(s) -1
    chars = list(s)
    
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]

        left += 1
        right -= 1

    return "".join(chars)


if __name__=="__main__":
    s = "hello"
    res = reverse_string_v2(s)
    print(res)
