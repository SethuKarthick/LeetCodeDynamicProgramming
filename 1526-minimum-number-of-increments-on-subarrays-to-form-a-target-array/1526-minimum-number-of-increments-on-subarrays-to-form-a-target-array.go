func minNumberOperations(target []int) int {
    crnt := 0
    prev := 0
    
    for i:= 0; i< len(target); i++{
        if target[i] > prev{
            crnt += (target[i] - prev) 
        }
        prev = target[i]
    }
    return crnt
}