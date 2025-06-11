fn readi() -> i32 {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().parse().unwrap()
}

fn read() -> String {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let q = readi();
    let mut stack = Vec::new();

    for i in 0..q {
        let input = read();

        match input.as_str() {
            "READ" => {
                println!("{}", stack.pop().unwrap())
            },
            _ => {
                let b = input.clone();
                stack.push(b)
            },
        }
    }
}