func minimumOneBitOperations(n int) int {
    // if n == 0{
    //     return 0
    // }
    // msbPos := 0
    // for i:= 31; i>=0; i--{
    //     if (n >> i) & 1 == 1{
    //         msbPos = i+1
    //         break
    //     }
    // }
    // if n == (1 << msbPos ){
    //     return msbPos
    // }
    // return 1 + minimumOneBitOperations((1 << msbPos) - 1 - n)
    // operations := 0
    // for n>0{
    //     if n & 1 == 1 {
    //         operations++
    //     }
    //     n >>=1
    // }
    // return operations 
    // if n == 0 {
    //     return 0
    // }
    
    // if n%2 == 0 {
    //     return minimumOneBitOperations(n / 2) + 1
    // } else {
    //     return minimumOneBitOperations((n-1) / 2) + 2
    // }
    var count, turn int 

    for i:=31; i>=0; i--{
        if n &(1 << i) > 0{
            if turn & 1 == 0{
                count += (1<<(i+1)) -1
            }else {
                count -= (1<<(i+1)) -1
            }
            turn++
        }
    }
    return count
}