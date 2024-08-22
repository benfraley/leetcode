/**
 * https://leetcode.com/problems/triangle/
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    // have to get the minimum possible total, so evaluate all possible totals
    // start at the bottom and compare
    triangle.reverse()
    for(i=0;i<triangle.length;i++)
    {
        for(j=0;j<triangle[i].length-1;j++)
        {
            if(triangle[i][j+1] !== undefined)
            {
                // determine which of the values is smaller and 
                // append it to the jth element in the next row
                if(triangle[i][j] <= triangle[i][j+1])
                {
                    triangle[i+1][j] = triangle[i+1][j] + triangle[i][j]
                }
                else
                {
                    triangle[i+1][j] = triangle[i+1][j] + triangle[i][j+1]
                }
            }
            else
            {
                // if j+1 doesnt exit use j
                triangle[i+1][j] = triangle[i+1][j] + triangle[i][j]
            }
        }
    }
    // reverse the array again and get the top element
    triangle.reverse()
    return triangle[0][0]
};