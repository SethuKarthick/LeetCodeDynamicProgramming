type node struct {
    row, col int
}

func minFallingPathSum(matrix [][]int) int {
    memo := make(map[node]int)

    var dp func(row, col int) int

    dp = func(row, col int) int {
        if col < 0 || col == len(matrix[0]){
            return math.MaxInt
        }
        if row == len(matrix)-1{
            return matrix[row][col]
        }
        if val, ok := memo[node{row, col}]; ok {
            return val
        }
        ans := math.MaxInt
        ans =  min(ans, dp(row+1, col))
        ans = min(ans, dp(row+1, col-1))
        ans = min(ans, dp(row+1, col+1))

        memo[node{row, col}] =  matrix[row][col] + ans

        return memo[node{row, col}]
        
    }
    answer := math.MaxInt
    for i:= 0; i< len(matrix); i++{
        answer = min(answer, dp(0, i))
    }
    return answer
}

func min(a, b int) int {
    if a < b {
        return a 
    }
    return b
}