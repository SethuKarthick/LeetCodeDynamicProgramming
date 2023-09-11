func numberOfArithmeticSlices(nums []int) int {
    n := len(nums)
    res := 0
    count := 0
    for i:= 2; i<n; i++{
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]{
            count++
        }else {
            count = 0
        }
        res += count
    }
    return res 
}