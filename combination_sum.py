# https://leetcode.com/problems/combination-sum/
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def makeDecisions(cand, i=0, desc=None, combo=[]):
            if desc == None:
                desc = []

            # print(desc, combo) # use to see it in action!

            # check if current decision tree branch totals the target
            # if so, add to combo and return
            if sum(desc) == target:
                combo.append(desc)
                return

            # if sum of the branch > target, return
            if sum(desc) > target:
                return

            # two possible decisions: add the current value or skip it and move the index up
            # this will lead to an array of smallest values possible values >= target
            # then move up to the next number in the candidate list
            desc1 = desc[:]
            desc2 = desc[:]
            desc1.append(cand[i])
            makeDecisions(cand, i, desc1, combo)
            if (i+1) < len(cand):
                makeDecisions(cand, i+1, desc2, combo)

            return combo

        return makeDecisions(candidates)

        