mod fizzbuzz;
mod reverse_integer;

fn main() {
    println!("FizzBuzz solution:");
    println!("{:?}", fizzbuzz::Solution::fizzbuzz());

    println!(" ");

    println!("Reverse integer solution:");
    let x = 500;
    println!("{}", reverse_integer::Solution::reverse_integer(x));
}
