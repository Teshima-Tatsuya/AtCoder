fn inputns() -> Vec<i32> {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut stdin = stdin.split_whitespace();
    stdin.map(|s| s.parse().unwrap()).collect()
}

fn solve(nums: Vec<i32>) -> i32 {
    nums[0] - nums[1] + nums[2]
}

fn main() {
    let nums: Vec<i32> = inputns();
    println!("{}", solve(nums));
}

#[cfg(test)]
#[test]
fn test() {
    assert_eq!(solve(vec![100, 10, 20]), 110);
}