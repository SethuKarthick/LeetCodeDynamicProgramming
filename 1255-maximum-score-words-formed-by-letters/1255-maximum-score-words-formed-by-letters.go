func maxScoreWords(words []string, letters []byte, score []int) int {
    freq := make([]int, 26)
    var ans int = 0
    for _, letter := range letters {freq[letter - 'a']++}
    dfs(0, words, freq, score, &ans, 0)
    return ans
}

func dfs(i int, words []string, freq []int, score []int, ans *int, curScore int){
    if i>= len(words) {return}
    var val int = 0
    var canTake bool = true
    for _, ch:= range words[i]{
        freq[ch - 'a']--
        val += score[ch - 'a']
        if freq[ch- 'a'] < 0 {canTake = false}
    }
    if canTake{
        if curScore + val > *ans { *ans = curScore + val}
        dfs(i+1, words, freq, score, ans, curScore+val)
    }
    for _, ch := range words[i]{
        freq[ch-'a']++
    }
    dfs(i+1, words, freq, score, ans, curScore)
}