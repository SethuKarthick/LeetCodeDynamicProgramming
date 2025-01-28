# # from collections import defaultdict
# # from typing import List

# # class Solution:
# #     def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
# #         prereq_map = defaultdict(list)  # course -> prereqs

# #         for prereq in prerequisites:
# #             prereq_map[prereq[1]].append(prereq[0])

# #         res = []
# #         memo = {}
# #         def dfs(course, prereq):
# #             if (course, prereq) in memo:
# #                 return memo[(course, prereq)]
            
# #             course_prereqs = prereq_map[course]
# #             for p in course_prereqs:
# #                 if p == prereq or dfs(p, prereq):
# #                     memo[(course, prereq)] = True
# #                     return True
            
# #             memo[(course, prereq)] = False
# #             return False
        
# #         return [dfs(query[1], query[0]) for query in queries]
# from collections import defaultdict, deque

# class Solution:
#     def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
#         # Step 1: Build the graph
#         adj = defaultdict(list)  # Adjacency list to store dependencies
#         for a, b in prerequisites:
#             adj[a].append(b)

#         # Step 2: Use BFS or DFS to find all reachable courses for each course
#         reachable = [set() for _ in range(numCourses)]  # This will store reachable courses for each course
        
#         def bfs(course):
#             visited = [False] * numCourses
#             queue = deque([course])
#             visited[course] = True
#             while queue:
#                 current = queue.popleft()
#                 for neighbor in adj[current]:
#                     if not visited[neighbor]:
#                         visited[neighbor] = True
#                         reachable[course].add(neighbor)
#                         queue.append(neighbor)

#         # BFS from each course to find reachable courses
#         for course in range(numCourses):
#             bfs(course)
        
#         # Step 3: Answer the queries
#         result = []
#         for u, v in queries:
#             result.append(u in reachable[v])  # Check if u is in the reachable set of v
        
#         return result

from collections import defaultdict, deque
from typing import List

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Step 1: Build the graph (in the correct direction)
        adj = defaultdict(list)  # course -> dependent courses
        for a, b in prerequisites:
            adj[b].append(a)  # b -> a means a depends on b
        
        # Step 2: Precompute reachable courses using DFS or BFS
        reachable = [set() for _ in range(numCourses)]  # List of reachable nodes for each course
        
        def dfs(course):
            visited = [False] * numCourses
            stack = [course]
            reachable_courses = set()
            while stack:
                curr = stack.pop()
                for next_course in adj[curr]:
                    if not visited[next_course]:
                        visited[next_course] = True
                        reachable_courses.add(next_course)
                        stack.append(next_course)
            return reachable_courses
        
        # Compute reachable courses for each course
        for course in range(numCourses):
            reachable[course] = dfs(course)
        
        # Step 3: Answer the queries
        result = []
        for u, v in queries:
            result.append(u in reachable[v])  # Check if u is reachable from v
        
        return result
