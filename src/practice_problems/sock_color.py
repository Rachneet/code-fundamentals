"""
Get pairs of socks
"""

from typing import List

def sock_color(socks: List):

    sock_drawer = dict()

    for s in socks:
        if s in sock_drawer:
            sock_drawer[s] += 1
        else:
            sock_drawer[s] = 1

    for k, v in sock_drawer.items():
        if v % 2 == 1:
            print(k, v)



if __name__ == "__main__":
    socks = [1, 2, 2, 1, 1, 3, 5, 1, 4, 4]
    res = sock_color(socks)
    print(res)
     