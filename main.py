class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        g = {}
        g = {heights[i]: names[i] for i in range(len(names))}
        od = collections.OrderedDict(sorted(g.items()))
        return ([v for k, v in od.items()][::-1]) 
