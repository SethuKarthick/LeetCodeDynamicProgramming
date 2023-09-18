func minFlipsMonoIncr(s string) int {
    // 00110
    occ_of_1 := 0

    flip := 0

    for _, char :=  range(s) {
        if char == '1'{
            occ_of_1 +=1
        }else{
            flip = min(flip+1, occ_of_1)
        }
    }
    return flip 
}

func min(x, y int) int {
    if x <= y{
        return x
    }
    return y
}