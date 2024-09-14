# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = []
        group = defaultdict()
        for i, size in enumerate(groupSizes):
            if size not in group.keys():
                group[size] = []
            if i not in group[size]:
                group[size].append(i)
            if len(group[size]) == size:
                groups.append(group[size])
                group[size] = [] 
        return groups