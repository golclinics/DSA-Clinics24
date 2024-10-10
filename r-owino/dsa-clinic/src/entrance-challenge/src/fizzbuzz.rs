/* The FizzBuzz problem */

pub struct Solution;

impl Solution {
    pub fn fizzbuzz() -> Vec<String> {
        let mut res = Vec::new();

        for i in 1..=100 {
            if i % 3 == 0 && i % 5 == 0 {
                res.push("FizzBuzz".to_string());
            } else if i % 3 == 0 {
                res.push("Fizz".to_string());
            } else if i % 5 == 0 {
                res.push("Buzz".to_string());
            } else {
                res.push(i.to_string())
            }
        }
        res
    }
}
