use crate::linked_list::ListNode;
/* 
206. Reverse Linked List

Example:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
given: 1 -> 2 -> 3 -> 4 -> 5
reverse: 5 -> 4 -> 3 -> 2 -> 1

Input: head = [1,2]
Output: [2,1]
given: 1 -> 2
reverse: 2 -> 1

Input: head = []
Output: [] 
*/

pub struct Solution;

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev: Option<Box<ListNode>> = None;
        let mut curr = head;

        while let Some(mut node) = curr {
            curr = node.next.take();
            node.next = prev;
            prev = Some(node);
        }
        prev
    }
}
