fn yesno(b: bool) {
    if b { println!("Yes") } else { println!("No") }
}

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
    let c = nums[2];

    yesno(c <= a + b)
}