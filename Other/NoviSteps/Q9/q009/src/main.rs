fn readi_l() -> Vec<i32> {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    stdin.split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect::<Vec<i32>>()
}

fn solve(num: Vec<i32>) -> i32 {
    num[0] + num[1]
}

fn main() {
    let nums = readi_l();
    let result = solve(nums);

    if result >= 10 {
        println!("error");
    } else {
        println!("{}",result);
    }
}