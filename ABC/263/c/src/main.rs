fn readi_l() -> Vec<i32> {
    let mut line = String::new();
    std::io::stdin().read_line(&mut line).unwrap();
    line.split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect::<Vec<i32>>()
}

fn dfs(arr: &mut Vec<i32>, start: i32, end: i32, m: i32) {
    // 終了条件
    if arr.len() as i32 == end {
        println!("{}", arr.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(" "));
        return;
    }
    // ループの処理
    for i in start..=m {
        arr.push(i);
        dfs(arr, i + 1, end, m); // ここで追加
        arr.pop(); // 追加した値を元に戻すことでdfsを実現
    }
}

fn main() {
    let input = readi_l();
    let n = input[0];
    let m = input[1];

    // 最初の数を1にしてスタート
    dfs(&mut vec![0; 0], 1, n, m);
}
