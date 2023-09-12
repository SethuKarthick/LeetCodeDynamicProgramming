func canPartition(nums []int) bool {
    sum := 0
    for _, num := range nums{
        sum += num
    }

    if sum & 0x1 == 1{
        return false 
    }
    sum = sum >> 1
    dp := make([]bool, sum+1)
    dp[0] = true

    for _, num := range nums {
        for i:=sum-num; i>=0; i--{
            if dp[i] == true{
                dp[i+num] = true
            }
            if dp[sum] == true{
                return true
            }
        }
    }
    return dp[sum]
}