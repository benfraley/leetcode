/**
 * https://leetcode.com/problems/majority-element/
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    freq = []
    for(i=0;i<nums.length;i++)
    {
        if(!freq[nums[i]])
        {
            freq[nums[i]] = 1
        }
        else
        {
            freq[nums[i]]++
        }
        if(freq[nums[i]] > (nums.length/2))
        {
            return nums[i]
        }
    }
};