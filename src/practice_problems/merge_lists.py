"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 is None:
        return l2
    elif l2 is None:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = mergeTwoLists(l1, l2.next)
        return l2


# Helper function to convert list to linked list
def create_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# Helper function to print linked list
def print_linked_list(head: Optional[ListNode]) -> None:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    print(values)


if __name__ == "__main__":
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    
    # Convert lists to linked lists
    l1 = create_linked_list(list1)
    l2 = create_linked_list(list2)
    
    res = mergeTwoLists(l1=l1, l2=l2)
    print_linked_list(res)  # [1, 1, 2, 3, 4, 4]