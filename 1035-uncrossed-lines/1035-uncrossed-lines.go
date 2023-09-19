func maxUncrossedLines(nums1 []int, nums2 []int) int {
    dp :=  make([][]int, len(nums1)+1)
    for i:= len(nums1); i>=0; i--{
        dp[i] = make([]int, len(nums2)+1)
    }

    for i:=len(nums1) -1; i>= 0; i--{
        for j:= len(nums2)-1; j>=0; j--{
            if nums1[i] == nums2[j]{
                dp[i][j] = 1 + dp[i+1][j+1]
            }else{
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
            }
        }
     }
     return dp[0][0]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}