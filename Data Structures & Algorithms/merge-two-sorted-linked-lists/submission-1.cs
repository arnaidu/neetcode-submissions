/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
 
public class Solution {
    public ListNode MergeTwoLists(ListNode list1, ListNode list2) {
        var outputList = new ListNode();
        var curr = outputList;
        while (list1 is not null && list2 is not null) {
            if (list1.val <= list2.val) {
                curr.next = list1;
                list1 = list1.next;
            }
            else {
                curr.next = list2;
                list2 = list2.next;
            }
            curr = curr.next;
        }

        var remainingList = list1 is not null ? list1 : list2;
        while (remainingList is not null) {
            curr.next = remainingList;
            remainingList = remainingList.next;
            curr = curr.next;
        }

        return outputList.next;
    }
}