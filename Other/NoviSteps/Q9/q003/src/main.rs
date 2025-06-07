fn read_grid() -> Vec<Vec<i32>> {
    let stdin = std::io::read_to_string(std::io::stdin()).unwrap();
    let lines: Vec<&str> = stdin.trim().split("\n").collect();
    
    let mut grid: Vec<Vec<i32>> = Vec::new();
    for line in lines {
        let row: Vec<i32> = line.split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        grid.push(row);
    }
    grid

}

fn solve(nums: Vec<Vec<i32>>) -> i32 {
    nums[0][0] * nums[1][1] - nums[0][1] * nums[1][0]
}

fn main() {
    let nums = read_grid();
    println!("{}", solve(nums));
}

#[cfg(test)]
#[test]
fn test() {
    assert_eq!(solve(vec![vec![1, 2], vec![3,4]]), -2);
}