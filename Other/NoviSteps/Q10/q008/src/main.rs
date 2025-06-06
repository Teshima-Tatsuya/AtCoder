fn solve(n: i32, m: i32, l: i32) -> i32 {
    n + m + l
}

fn main() {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let mut stdin = stdin.split_whitespace();
    let n:i32 = stdin.next().unwrap().parse().unwrap();
    let m:i32 = stdin.next().unwrap().parse().unwrap();
    let l:i32 = stdin.next().unwrap().parse().unwrap();
    println!("{}", solve(n, m, l));
}

#[cfg(test)]
#[test]
fn test() {
    assert_eq!(solve(5, 10, 20), 35);
}