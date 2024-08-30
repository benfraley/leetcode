# https://leetcode.com/problems/count-and-say/
class Solution:
    def countAndSay(self, n: int) -> str:
        
        def rle(string):
            # count the consecutive integers in the string
            i = 0
            counts = []
            c = 1
            while i < len(string):
                if i + 1 < len(string) and string[i] == string[i+1]: # check if the same integer
                    c += 1
                else: # once we find a new number, add tuple to counts list
                    counts.append((c, string[i]))
                    c = 1 # reset the count
                i += 1 # next index

            ret = ""
            for t in counts:
                ret += str(t[0]) + str(t[1]) # append the count and the integer to the return
            return ret 

        string = str(1)
        if n != 1:
            for i in range(0, n-1):
                string = rle(string) # recursively add find the rle value

        return string