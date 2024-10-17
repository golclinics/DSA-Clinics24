mod fizzbuzz;
mod reverse_integer;
mod power_of_two;

fn main() {
    println!("FizzBuzz solution:");
    println!("{:?}", fizzbuzz::Solution::fizzbuzz());

    println!(" ");

    println!("Reverse integer solution:");
    let x = 500;
    println!("{}", reverse_integer::Solution::reverse_integer(x));

    println!(" ");
    println!("Power of two solution:");
    let n = 32;
    println!("{}", power_of_two::Solution::is_power_of_two(n));
}
