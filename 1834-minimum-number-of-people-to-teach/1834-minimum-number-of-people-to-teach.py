class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        
        def can_talk(u, v):
            return bool(set(languages[u-1]) & set(languages[v-1]))

        need_teach = set()
        for u, v in friendships:
            if not can_talk(u, v):
                need_teach.add(u)
                need_teach.add(v)
            
        if not need_teach:
            return 0

        lang_count = [0] * (n+1)
        for i in need_teach:
            for l in languages[i-1]:
                lang_count[l] += 1

        return len(need_teach) - max(lang_count)


