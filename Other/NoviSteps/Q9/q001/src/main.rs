fn inputns() -> Vec<i32> {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut stdin = stdin.split_whitespace();
    stdin.map(|s| s.parse().unwrap()).collect()
}

fn solve(nums: Vec<i32>) -> i32 {
    nums[0] + nums[0].pow(2) + nums[0].pow(3)
}

fn main() {
    let nums: Vec<i32> = inputns();
    println!("{}", solve(nums));
}

#[cfg(test)]
#[test]
fn test() {
    assert_eq!(solve(vec![2]), 14);
}