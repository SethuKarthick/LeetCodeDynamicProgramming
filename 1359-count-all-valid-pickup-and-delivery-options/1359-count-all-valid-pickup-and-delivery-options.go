func countOrders(n int) int {
    MOD := 1000000007

    slots :=  2* n
    res := 1
    for slots > 0{
        valid_choices := slots * (slots - 1) / 2
        res = (res*valid_choices) % MOD
        slots -= 2 
    }
    return res

    // for i:= 2; i<= n; i++{
    //     slots := 2*i
    //     valid_choices := i*(slots-1)
    //     res = (res*valid_choices) % MOD
    // }
    // return res 
}