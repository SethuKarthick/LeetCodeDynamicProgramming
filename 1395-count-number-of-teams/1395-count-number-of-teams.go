func numTeams(rating []int) int {
    res :=  0
    
    for i:= 1; i< len(rating)-1; i++{
        mid := rating[i]
        descLeft := 0
        ascLeft := 0
        for j:= 0; j< i; j++{
            if rating[j] < mid{
                descLeft++
            }
            if rating[j] > mid{
                ascLeft++
            }
        }

        descRight := 0
        ascRight := 0
        for k:= i+1; k< len(rating); k++{
            if rating[k] < mid {
                descRight++
            }
            if rating[k] > mid{
                ascRight++
            }
        }
        res += descLeft*ascRight + ascLeft*descRight
    }
    return res
}