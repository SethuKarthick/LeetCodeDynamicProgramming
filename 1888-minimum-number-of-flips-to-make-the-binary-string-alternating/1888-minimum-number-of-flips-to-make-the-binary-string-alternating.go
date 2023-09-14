func minFlips(s string) int {
    s += s
    target_1 := make([]byte, len(s))
    target_2 := make([]byte, len(s))

    for i:= 0; i<len(s); i++{
        if i%2 == 0{
            target_1[i] = 0
            target_2[i] = 1
        }else {
            target_1[i] = 1
            target_2[i] = 0
        }
    }
    res := len(s)
    diff1, diff2 := 0, 0

    l:=0
    for r:=0; r<len(s); r++{
        if target_1[r] != (s[r]-'0'){
            diff1++
        }
        if target_2[r] != (s[r]-'0'){
            diff2++
        }
        if (r-l+1) > (len(s)/2){
            if target_1[l] != (s[l]-'0'){
                diff1--
            }
            if target_2[l] != (s[l]-'0'){
                diff2--
            }
            l++
        }
        if (r-l+1) == (len(s)/2){
            res = min(res, min(diff1,diff2))
        }
    }
    return res
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}