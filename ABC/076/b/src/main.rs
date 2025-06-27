fn readi() -> i32 {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.trim().parse().unwrap()
}

fn main() {
    let n = readi();
    let k = readi();

    // 初期値1で始まる
    let mut num = 1;

    for i in 0..n {
        if num <= k {
            num *= 2;
        } else {
            num += k;
        }
    }
    println!("{}", num);
}
