# https://leetcode.com/problems/lucky-numbers-in-a-matrix
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        luckys = []
        # find mins
        mins, min_index = [], []
        for row in matrix: # load all the mins for a row and their index
            mins.append(min(row))
            min_index.append(row.index(min(row)))

        # loop through all the min_index y values, compare against 
        # the min[i] value relating to that index
        for i, index in enumerate(min_index):
            col = []
            for row in matrix:
                col.append(row[index])
            print(max(col), mins[i])
            # if these are the same, it's a lucky number!
            if max(col) == mins[i]:
                luckys.append(max(col))
        return luckys
                
        