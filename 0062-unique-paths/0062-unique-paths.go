func uniquePaths(m int, n int) int {
    // ans := 1
    // for i:=1; i<=m-1; i++{
    //     ans = ans*(n-1+i) / i
    // }
    // return ans
    
// 3, 2
// i = 1
// 1 * (2-1+1) /1
// ans = 2

// i = 2
// 2*(2-1+2) / 2
// ans = 3
    
    dp := make([][]int, m)
    for i:= range dp{
        dp[i] = make([]int, n)
    }

    for i:=0; i<m; i++{
        dp[i][0] = 1
    }
    for j:=0; j<n; j++{
        dp[0][j] = 1
    }
    for i:=1; i<m; i++{
        for j:=1; j<n; j++{
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        }
    }
    return dp[m-1][n-1]
}



// dp -> [
//     [0 0] 
//     [0 0] 
//     [0 0]
// ]
// dp -> [
//     [1 0] 
//     [1 0] 
//     [1 0]
// ]
// dp -> [
//     [1 1] 
//     [1 0] 
//     [1 0]
// ]
// dp -> [
//     [1 1] 
//     [1 2] 
//     [1 3]
// ]


