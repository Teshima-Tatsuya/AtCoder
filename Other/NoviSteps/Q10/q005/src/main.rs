fn solve(n: i32) -> i32 {
    n * 24
}

fn main() {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut stdin = stdin.split_whitespace();
    let n:i32 = stdin.next().unwrap().parse().unwrap();
    println!("{}", solve(n));
}

#[cfg(test)]
#[test]
fn test() {
    assert_eq!(solve(5), 120);
}