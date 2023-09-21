func lengthOfLIS(nums []int, k int) int {
    lis := make([]int, 1e5+1)

    for i:= range nums{
        if nums[i] >= k{
            lis[nums[i]] = max(lis[nums[i] - k : nums[i]]...) + 1
        }else {
            lis[nums[i]] = max(lis[:nums[i]]...) + 1
        }
    }
    return max(lis...)
}

func max(a ...int) int {
    max :=  a[0]
    for i:= range a {
        if a[i] > max{
            max =  a[i]
        }
    }
    return max
}