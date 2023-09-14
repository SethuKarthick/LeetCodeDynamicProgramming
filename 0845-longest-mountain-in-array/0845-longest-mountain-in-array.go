func longestMountain(arr []int) int {
    if len(arr) < 3{
        return 0
    }

    var count int 
    for i:= 1; i< len(arr)-1; i++{
        if arr[i-1] < arr[i] && arr[i] > arr[i+1]{
            leftIdx, rightIdx := i-1, i+1
            for ; leftIdx>0 && arr[leftIdx-1] < arr[leftIdx]; leftIdx--{}
            for ; rightIdx<len(arr)-1 && arr[rightIdx] > arr[rightIdx+1]; rightIdx++{}
            count = max(count, (rightIdx-leftIdx)+1) 
        }
    }
    return count
}

func max(a, b int)int {
    if a > b{
        return a
    }
    return b
}