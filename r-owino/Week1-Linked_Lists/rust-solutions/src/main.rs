mod linked_list;
mod pairwise_swap;
mod reverse_list;

use linked_list::{vec_to_linked_list, linked_list_to_vec};
use pairwise_swap::Solution as SwapSolution;
use reverse_list::Solution as ReverseSolution;

fn main() {
    println!("Reverse a list:");
    let head = vec_to_linked_list(vec![1, 2, 3, 4]);
    println!("{:?}", linked_list_to_vec(ReverseSolution::reverse_list(head)));

    println!("\nSwap pair nodes:");
    let head = vec_to_linked_list(vec![1, 2, 3, 4, 5]);
    println!("{:?}", linked_list_to_vec(SwapSolution::swap_pairs(head)))
}
