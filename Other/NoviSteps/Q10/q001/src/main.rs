// https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_a
use std::io;

fn main(){
  // 1つ目の整数を受け入れる
  let mut input = String::new();
  io::stdin().read_line(&mut input).expect("Failed");
  let n: i32 = input.trim().parse().unwrap();

  println!("{}", n + 5);
}