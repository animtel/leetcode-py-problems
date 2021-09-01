# 21. Merge Two Sorted Lists: https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional
import copy

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
    if head.val is None:
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
    def get_last(self, head: Optional[ListNode]):
        if head.next is None: return head
        return self.get_last(head.next)

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 is None or l2 is None: return []

        if l1.next is None and l2.next is None:
            if l1.val is None and l2.val is not None: return l2
            if l2.val is None and l1.val is not None: return l1

        temp_l1 = l1

        stack = []

        self.get_last(l1).next = l2

        while temp_l1 is not None:
            stack.append(temp_l1.val)
            temp_l1 = temp_l1.next

        stack = sorted(stack)
        result = ListNode(stack[0])

        for i in stack[1:]:
            latest = self.get_last(result)
            latest.next = ListNode(i)

        return result


class Solution_00_1:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return l1

        merged_list = ListNode(-1)
        dummy_merge_list = merged_list

        while l1 or l2:
            if l1 and not l2:
                dummy_merge_list.val = l1.val
                l1 = l1.next
            elif not l1 and l2:
                dummy_merge_list.val = l2.val
                l2 = l2.next
            else:
                if l1.val < l2.val:
                    dummy_merge_list.val = l1.val
                    l1 = l1.next
                else:
                    dummy_merge_list.val = l2.val
                    l2 = l2.next
            if l1 or l2:
                dummy_merge_list.next = ListNode(None)
                dummy_merge_list = dummy_merge_list.next
        return merged_list


def check_hypothesis_for(hypothesis_func, given, should):
    processed = hypothesis_func(*given)
    processed = create_arr_from_list(processed)
    assert processed == should, f'Wrong hypothesis for given:{given}, returned: {processed}, should be {should}!'


if __name__ == '__main__':
    hypothesis = Solution_00_1().mergeTwoLists

    a = create_list_from_arr([1, 2, 4])
    b = create_list_from_arr([1, 3, 4])

    a = create_list_from_arr([1])
    b = create_list_from_arr([1])
    check_hypothesis_for(hypothesis, (a, b), [1, 1])

    # a = create_list_from_arr([])
    # b = create_list_from_arr([])
    # check_hypothesis_for(hypothesis, (a, b), [])

# ------------------------------------

    print(create_arr_from_list(a))
    print(create_arr_from_list(a_d_copied))
    print(create_arr_from_list(a_s_copied))

    # check_hypothesis_for(hypothesis, (a, b), [1, 1, 2, 3, 4, 4])
    #
    # a = create_list_from_arr([])
    # b = create_list_from_arr([])
    # check_hypothesis_for(hypothesis, (a, b), [])


