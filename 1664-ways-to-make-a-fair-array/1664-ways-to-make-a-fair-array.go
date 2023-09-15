func waysToMakeFair(nums []int) int {
    ans, left, right := 0, [2]int{}, [2]int{}

    for i, v := range nums{
        right[i%2] += v
    }
    for i, v := range nums{
        right[i%2] -= v
        if left[0] + right[1] == left[1] + right[0]{
            ans++
        }
        left[i%2] += v
    }
    return ans
}