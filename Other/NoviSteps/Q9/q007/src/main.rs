
fn readi_l() -> Vec<i32> {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    stdin.split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect::<Vec<i32>>()
}

fn solve(nums: Vec<i32>) -> f64 {
    let A = nums[0];
    let B = nums[1];
    let C = (A - B) as f64 / 3.0 + B as f64;
    C
}

fn main() {
    let nums = readi_l();
    println!("{}", solve(nums));
}