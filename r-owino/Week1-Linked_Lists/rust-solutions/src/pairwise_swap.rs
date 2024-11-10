use crate::linked_list::ListNode;
/* 
24. Swap Nodes in Pairs

Example:
Input: head = [1,2,3,4]
Output: [2,1,4,3]
given: 1 -> 2 -> 3 -> 4
swap: 2 -> 1 -> 4 -> 3

Input: head = [1,2,3]
Output: [2,1,3]
given: 1 -> 2 -> 3
swap: 2 -> 1 -> 3 
*/

pub struct Solution;

impl Solution {
    pub fn swap_pairs(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
		// create a dummy node
		let mut dummy = Some(Box::new(ListNode { val: 0, next: head}));
		let mut prev = dummy.as_mut();

		while let Some(node) = prev {
			// check there are 2 nodes to swap
			if node.next.is_some() && node.next.as_ref()?.next.is_some() {
				let mut first = node.next.take().unwrap();
				let mut second = first.next.take().unwrap();

				// perform the swap
				node.next = Some(second.clone());
				let first = Some(Box::new(ListNode {
					val: first.val,
					next: second.next.take(),
				}));
				node.next.as_mut()?.next = first;

				// next pair swap
				prev = node.next.as_mut()?.next.as_mut();
			} else {
				break;
			}
		}
		dummy.unwrap().next
	}
}
