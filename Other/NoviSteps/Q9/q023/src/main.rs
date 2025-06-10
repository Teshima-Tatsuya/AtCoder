fn yesno(b: bool) {
    if b { println!("Odd") } else { println!("Even") }
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

    yesno((a * b) % 2 != 0);
}