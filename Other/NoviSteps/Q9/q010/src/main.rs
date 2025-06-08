fn readi() -> i32 {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().parse().unwrap()
}

fn main() {
    let n = readi();
    if n == 1 {
        println!("Hello World");
    } else {
        let a = readi();
        let b = readi();
        println!("{}", a + b);
    }
}