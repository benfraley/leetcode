/**
 * https://leetcode.com/problems/pascals-triangle/
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows)
{
    tri = [[1]]
    for(i=1; i<numRows;i++)
    {
        tri[i] = []
        // next row has a length of i+1
        tri[i][0] = 1 // first element always 1
        for(j=1;j<i;j++)
        {
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j] // add the values to the top left and top right
        }
        tri[i][i] = 1 // last element always 1
    }
    return tri

};