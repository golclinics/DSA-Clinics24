// definition for a singly-linked list
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
   pub val: i32,
   pub next: Option<Box<ListNode>>,
}

impl ListNode {
   #[inline]
   fn new(val: i32) -> Self {
       ListNode {
           next: None,
           val
       }
   }
}

struct Solution;

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

// convert Vec<i32> to Option<Box<ListNode>>
fn vec_to_linked_list(values: Vec<i32>) -> Option<Box<ListNode>> {
    let mut curr = None;
    for &val in values.iter().rev() {
        let mut new_node = Box::new(ListNode::new(val));
        new_node.next = curr;
        curr = Some(new_node);
    }
    curr
}

// convert Option<Box<ListNode>> to Vec<i32>
fn linked_list_to_vec(mut head: Option<Box<ListNode>>) -> Vec<i32> {
    let mut values = vec![];
    while let Some(node) = head {
        values.push(node.val);
        head = node.next;
    }
    values
}

fn main() {
    let head = vec_to_linked_list(vec![4]);
    let reversed_vec = linked_list_to_vec(Solution::reverse_list(head));
    println!("{:?}", reversed_vec);
}
