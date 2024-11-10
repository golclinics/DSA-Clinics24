/* Contains the linked list definition and shared functions */

// defintion for a singly linked list
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

// convert Vec<i32> to Option<Box<ListNode>>
pub fn vec_to_linked_list(values: Vec<i32>) -> Option<Box<ListNode>> {
    let mut curr = None;
    for &val in values.iter().rev() {
        let mut new_node = Box::new(ListNode::new(val));
        new_node.next = curr;
        curr = Some(new_node);
    }
    curr
}

// convert Option<Box<ListNode>> to Vec<i32>
pub fn linked_list_to_vec(mut head: Option<Box<ListNode>>) -> Vec<i32> {
    let mut values = vec![];
    while let Some(node) = head {
        values.push(node.val);
        head = node.next;
    }
    values
}
