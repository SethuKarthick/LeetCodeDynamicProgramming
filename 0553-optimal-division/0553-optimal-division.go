func optimalDivision(nums []int) string {
    n :=  len(nums)
    if n == 0 {
        return ""
    }
    if n == 1{
        return strconv.Itoa(nums[0])
    }
    if n ==2{
        return strconv.Itoa(nums[0])+ "/" + strconv.Itoa(nums[1])
    }
    res := strconv.Itoa(nums[0])+ "/(" + strconv.Itoa(nums[1])

    for i:=2; i<n; i++{
        res += "/"+strconv.Itoa(nums[i]) 
    }

    res += ")"
    return res
}