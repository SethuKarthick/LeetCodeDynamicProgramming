func countArrangement(n int) int {
    count := 0
		visited := make([]bool, n+1)

		var backTrack func(int)
		backTrack = func(k int) {
			if k > n {
				count++
			}
			for i:= 1; i<= n ; i++{
				if !visited[i] && (i%k == 0 || k%i == 0){
					visited[i] = true
					backTrack(k+1)
					visited[i] = false
				}
			}
		}
		backTrack(1)
		return count
}