# 21. Merge Two Sorted Lists: https://leetcode.com/problems/merge-two-sorted-lists/
from functools import reduce
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def append_to(head, val):
    tmp = head
    while tmp.next is not None:
        tmp = tmp.next

    tmp.next = ListNode(val)
    return head

def create_arr_from_list(head):
    if head.val == None:
        return []

    arr = []
    tmp = head
    while tmp.next is not None:
        arr.append(tmp.val)
        tmp = tmp.next

    arr.append(tmp.val)

    return arr


def create_list_from_arr(arr):
    if not arr:
        return ListNode(None, None)

    head = ListNode(arr[0])
    for i in arr[1:]:
        append_to(head, i)

    return head


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return ListNode(None, None)


def check_hypothesis_for(hypothesis_func, given, should):
    processed = hypothesis_func(*given)
    processed = create_arr_from_list(processed)
    assert processed == should, f'Wrong hypothesis for given:{given}, returned: {processed}, should be {should}!'

if __name__ == '__main__':
    hypothesis = Solution().mergeTwoLists

    a = create_list_from_arr([1, 2, 4])
    b = create_list_from_arr([1, 3, 4])
    check_hypothesis_for(hypothesis, (a, b), [1, 1, 2, 3, 4, 4])

    a = create_list_from_arr([])
    b = create_list_from_arr([])
    check_hypothesis_for(hypothesis, (a, b), [])


