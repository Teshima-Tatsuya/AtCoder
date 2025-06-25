fn readi() -> i32 {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().parse().unwrap()
}

fn readi_l() -> Vec<i32> {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect::<Vec<i32>>()
}

fn main() {
    let n = readi();
    let a = readi_l();
    let mut stack: Vec<i32> = Vec::new();

    for i in 0..n {
        stack.push(a[i as usize].clone());
        while true {
            if stack.len() <= 1 {
                break;
            } else if stack[stack.len() - 1] != stack[stack.len() - 2] {
                break;
            } else {
                let t1 = stack.pop().unwrap();
                let t2 = stack.pop().unwrap();
                stack.push(t1 + 1);
            }
        }
    }

    println!("{}", stack.len() as i32);
}