func canPartitionKSubsets(nums []int, k int) bool {
    l := len(nums)
    if k > l {
        return false
    }
    s:= 0
    for i:=0; i<l; i++{
        s= s+nums[i]
    }

    if s%k != 0{
        return false 
    }
    expectedSum := s/k

    used := make([]bool, l)
    sort.Slice(nums, func(i, j int) bool{
        return nums[i] > nums[j]
    })
    return backTrack(0, 0, k-1, expectedSum, &used, &nums)
}

func backTrack(startIdx, currentSum, kleft, expectedSum int, used *[]bool, nums *[]int) bool{
    l := len(*nums)
    if kleft == 0{
        return true
    }
    if currentSum == expectedSum {
        return backTrack(0, 0, kleft-1, expectedSum, used, nums)
    }
    if currentSum > expectedSum || startIdx >= l{
        return false
    }
    for i:= startIdx; i<l; i++{
        if !(*used)[i] {
            (*used)[i] = true
            if backTrack(i+1, currentSum+(*nums)[i], kleft, expectedSum, used, nums){
                return true
            }
            (*used)[i] =  false
        }
    }
    return false 
}