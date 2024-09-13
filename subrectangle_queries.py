# https://leetcode.com/problems/subrectangle-queries/solutions/5782951/python-solution-o-n/ - My post on my solution
# > 98.11%, 115ms, 18.66mb
class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        self.rect = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        # can update the entire row in one swoop with list slices
        # dont have to iterate over each column that way
        newValArr = [newValue] * (col2-col1+1)
        for row in range(row1, row2+1):
            self.rect[row][col1:col2+1] = newValArr

    def getValue(self, row: int, col: int) -> int:
        return self.rect[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)