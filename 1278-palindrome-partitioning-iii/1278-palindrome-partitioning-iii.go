func palindromePartition(s string, k int) int {
    n := len(s)


    palindromeScore :=  func(substring string) int {
      score := 0
      for i:= 0; i< len(substring)/2; i++{
        if substring[i] != substring[len(substring)-1-i]{
          score++
        }
      }
      return score
    }

    dp := make([][]int, n+1)
    for i:=0; i<=n; i++{
      dp[i] =  make([]int, k+1)
      for j:=0; j<=k; j++{
        dp[i][j] = math.MaxInt32
      }
    }

    dp[0][0] = 0
    for i:= 1; i<=n; i++{
      for j:= 1; j<= k; j++{
        for x:= 0; x<i; x++{
          dp[i][j] = min(dp[i][j], dp[x][j-1]+palindromeScore(s[x:i]))
        }
      }
    }
    return dp[n][k]
}

func min(a, b int) int {
  if a < b {
    return a 
  }
  return b
}