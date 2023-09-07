func longestSubarray(nums []int) int {
    // [0,1,1,1,0,1,1,0,1]
    right, left, zeroesCount := 0, 0, 0

    for ;right < len(nums); right++{
        if nums[right] == 0{
            zeroesCount++
        }
        if zeroesCount > 1{
            if nums[left] == 0{
                zeroesCount--
            }
            left++
        }
    }
    return right-left-1
}
// r = 0
// 0 + 1 - 0
// z = 1

// r =1
// 1+ (1 - 1)
// z = 1

// r = 2
// 1 + (1 - 1)
// z = 1

// r = 3
// 1+(1-1)
// z = 1

// r = 4
// 1 + 1 - 0
// z = 2

// 2 - (1 - 0)
// z = 1
// l = 1

// r = 5
// 1+(1-1)
// z = 1

// r = 6
// 1+(1 - 1)
// z = 1

// r = 7
// 1+(1-0)
// z = 2

// 2 - (1 - 1)
// z = 2
// l = 2

// r = 8
// 2 + (1- 1)
// z = 2

// 2 - (1 - 1)
// z = 2

// 8 - 2 - 1


