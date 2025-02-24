class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        
        # Build graph
        graph = defaultdict(list)
        for a, b in edges: 
            graph[a].append(b)
            graph[b].append(a)
        
        # Bobs Path
        bob_tracker = {}
        
        # Finds Bob's Path to root
        def backtrack_bob(curr, time): 
            bob_tracker[curr] = time

            if curr == 0: 
                return True
            
            for nei in graph[curr]: 
                if nei not in bob_tracker:
                    if backtrack_bob(nei, time+1): return True 
                    
            del bob_tracker[curr]
            return False
        
        backtrack_bob(bob, 0)

        # Finds Alice optimal leaf path
        def backtrack_alice(curr, income, time, path): 
            new_income = amount[curr]
            
            #checks if Bob has been to node <= curr time
            if curr in bob_tracker: 
                if bob_tracker[curr] == time: 
                    new_income //= 2
                elif bob_tracker[curr] < time: 
                    new_income = 0
            
            income += new_income

            # Checks if leaf node
            if curr != 0 and len(graph[curr]) == 1:
                nonlocal ans 
                ans = max(ans, income)
            
            path.add(curr)
            for nei in graph[curr]:
                if nei not in path: 
                    backtrack_alice(nei, income, time+1, path)
            
            path.remove(curr)
            return 
        
        ans = float(-inf)
        backtrack_alice(0, 0, 0, set())
        return ans
        