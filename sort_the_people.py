# https://leetcode.com/problems/sort-the-people
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = []
        for k, v in enumerate(names):
            people.append((v, heights[k]))
        people = sorted(people, key=lambda item:(-item[1]))
        ret = []
        for p in people:
            ret.append(p[0])
        return ret