func calculateMinimumHP(dungeon [][]int) int {
    
   dp := make([][]int, len(dungeon))

   for i:= range dp{
       dp[i] = make([]int, len(dungeon[0]))
   }
   dp = dungeon

   n := len(dungeon[0]) - 1
   m := len(dungeon) -1

   dp[m][n] = max(1, 1-dungeon[m][n])

   for r:= m-1; r>=0; r--{
       dp[r][n] = max(1, dp[r+1][n]-dp[r][n])
   }
   for c:=n-1; c>=0; c--{
       dp[m][c] = max(1, dp[m][c+1]-dp[m][c])
   }

   for r:=m-1; r>=0; r--{
       for c:=n-1; c>=0; c--{
           dp[r][c] = max(1, min(dp[r+1][c], dp[r][c+1])-dp[r][c]) 
       }
   }
   return dp[0][0]


}

func max(a, b int) int{
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a 
    }
    return b
}