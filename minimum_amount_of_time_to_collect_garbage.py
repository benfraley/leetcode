# https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/solutions/5792336/confusing-question-hopefully-a-good-explanation/
class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        trucks = ["M", "P", "G"] # what each truck picks up
        time = 0

        for truck in trucks:
            loc = 0 # starting position
            for i in range(len(garbage)):
                # do we need to go here?
                if truck in garbage[i]:
                    # print(truck, " picking up ", garbage[i].count(truck), " from ", loc, " to ", i)
                    time += garbage[i].count(truck)
                    # if not there, move there
                    while loc != i:
                        # print(loc, " to ", loc+1, ", adding ", travel[loc])
                        time += travel[loc]
                        loc += 1
        return time