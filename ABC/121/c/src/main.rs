fn readi_l() -> Vec<i64> {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect::<Vec<i64>>()
}

fn main() {
    let input = readi_l();
    let n = input[0];
    let m = input[1];
    let mut juices: Vec<(i64, i64)> = Vec::new();

    // 全部を一気に読み込む
    for i in 0..n {
        let input = readi_l();
        let a = input[0];
        let b = input[1];
        juices.push((a, b));
    }

    juices.sort_by(|a, b| a.0.cmp(&b.0));

    let mut buy = 0;
    let mut cost = 0;
    for juice in juices {
        if buy <= m {
            let (a, b) = juice;
            if b <= m - buy {
                cost += a * b;
                buy += b;
            } else {
                let remaining = m - buy;
                cost += a * remaining;
                buy += remaining;
                break;
            }
        }
    }
    println!("{}", cost);
}
