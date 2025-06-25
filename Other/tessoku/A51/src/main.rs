fn readi() -> i32 {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().parse().unwrap()
}

fn readi_l() -> Vec<String> {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.split_whitespace()
        .map(|s| s.to_string())
        .collect::<Vec<String>>()
}

fn main() {
    let q = readi();
    let mut stack = Vec::new();

    for i in 0..q {
        let input = readi_l();
        let a = input[0].parse::<i32>().unwrap();

        match a {
            1 => {
                let b = input[1].clone();
                stack.push(b)
            },
            2 => println!("{}", stack.last().unwrap()),
            3 => { stack.pop(); },
            _ => println!("Invalid operation"),
        }
    }
}