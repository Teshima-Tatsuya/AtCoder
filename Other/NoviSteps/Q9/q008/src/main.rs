fn yesno(b: bool) -> &'static str {
    if b { "Yes" } else { "No" }
}

fn readi() -> i32 {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut stdin = stdin.split_whitespace();
    stdin.next().unwrap().parse().unwrap()
}

fn solve(num: i32) -> &'static str {
    yesno(num >= 30)
}

fn main() {
    let num = readi();
    println!("{}", solve(num));
}