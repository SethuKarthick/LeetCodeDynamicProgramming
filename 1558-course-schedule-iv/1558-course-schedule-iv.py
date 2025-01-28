class Solution:
    def checkIfPrerequisite(self, _: int, p: List[List[int]], q: List[List[int]]) -> List[bool]:
        g = {v:{u for _,u in w} for v,w in groupby(p,itemgetter(0))}
        f = cache(lambda v,u:u in g.get(v,[]) or any(f(i,u) for i in g.get(v,[])))
        return [*starmap(f, q)]