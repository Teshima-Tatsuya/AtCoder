fn readi() -> i32 {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().parse().unwrap()
}

fn main() {
    let x = readi();
    let a = readi();
    let b = readi();

    println!("{}", (x - a) % b)
}