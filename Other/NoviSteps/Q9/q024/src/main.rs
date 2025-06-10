fn readi_l() -> Vec<i32> {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect::<Vec<i32>>()
}

fn main() {
    let nums = readi_l();
    let a = nums[0];
    let b = nums[1];

    println!("{}", std::cmp::max(a + b, a - b));
    println!("{}", std::cmp::min(a + b, a - b));
}