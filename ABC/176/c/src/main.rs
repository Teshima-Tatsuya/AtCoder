fn readi() -> i64 {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().parse().unwrap()
}

fn readi_l() -> Vec<i64> {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect::<Vec<i64>>()
}

fn main() {
    let n = readi();
    let a = readi_l();
    let mut step: i64 = 0;
    let mut cur_max: i64 = a[0];

    // start from 2nd
    for i in 1..n {
        // 
        if a[i as usize] < cur_max {
            step += cur_max - a[i as usize];
        } else {
            cur_max = a[i as usize];
        }

    }
    println!("{}", step);
}
