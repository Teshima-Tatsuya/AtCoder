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
    // 連続する数、プッシュする数
    let mut stack: Vec<(i32, i32)> = Vec::new();

    for i in 0..n {
        let a_c = a[i as usize];
        if stack.len() < 1 {
            stack.push((1, a_c));
        } else {
            if let Some((vn, v)) = stack.last().copied() {
                if v == a_c {
                    stack.push((vn + 1, a_c));
                    if a_c == vn + 1 {
                        for _ in 0..a_c {
                            stack.pop();
                        }
                    }
                } else {
                    stack.push((1, a_c));
                }
            }
        }
        println!("{}", stack.len() as i32);
    }

}