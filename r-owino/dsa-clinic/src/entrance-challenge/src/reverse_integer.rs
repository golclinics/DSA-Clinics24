/*Reverses an integer*/

pub struct Solution;

impl Solution {
    pub fn reverse_integer(x: i32) -> i32 {
        let mut res: i32 = 0;
        let sign = if x < 0 { -1 } else { 1 };
        let mut x = x.abs();

        while x != 0 {
            let remainder = x % 10;
            res = res * 10 + remainder;
            x /= 10;
        }

        res * sign
    }
}
