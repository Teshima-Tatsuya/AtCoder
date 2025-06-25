fn reads() -> String {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let s = reads();
    let mut stack: Vec<i32> = Vec::new();

    for (i, c) in s.chars().enumerate() {
        if c == '(' {
            stack.push(i as i32);
            continue;
        } else {
            println!("{} {}", stack.pop().unwrap() + 1, i + 1);
        }
    }
}