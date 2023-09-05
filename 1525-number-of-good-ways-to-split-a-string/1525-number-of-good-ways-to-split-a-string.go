func numSplits(s string) int {
    lmp, rmp := make(map[string]int), make(map[string]int)

    for _, v := range s{
        rmp[string(v)]++
    }
    var count int 
    for _, v:= range s{
        elem := string(v)
        lmp[elem]++
        rmp[elem]--
        if rmp[elem] == 0{
            delete(rmp, elem)
        }
        if len(lmp) == len(rmp){
            count++
        }
    }
    return count
}