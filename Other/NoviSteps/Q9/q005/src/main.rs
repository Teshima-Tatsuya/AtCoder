fn readi() -> i32 {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut stdin = stdin.split_whitespace();
    stdin.next().unwrap().parse().unwrap()
}

fn solve(r: i32) -> f64 {
    2 as f64 * std::f64::consts::PI * r as f64
}

fn main() {
    let r = readi();
    println!("{}", solve(r));
}