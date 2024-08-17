<?php
// https://leetcode.com/problems/remove-element/
// removes an element from an array in place, returns the number of elements removed
// runtime 8ms, beats 52.89%, memory 53.55%
class Solution {

    /**
     * @param Integer[] $nums
     * @param Integer $val
     * @return Integer
     */
    function removeElement(&$nums, $val) {
        // edge cases
        if(count($nums) == 0) {
            return 0;
        }
        if(count($nums) == 1) {
            if($nums[0] == $val)
            {
                return 0;
            } 
            else
            {
                return 1;
            }
        }
        // binary search for val in nums
        sort($nums);
        $left = 0;
        $right = count($nums) - 1;
        $k = 0;
        while($left <= $right)
        {
            $middle = floor(($left + $right) / 2);
            if($nums[$middle] == $val)
            {
                while($nums[$middle] == $val) // we found it
                {
                    $nums[$middle] = "_"; // remove the value and check either side of it
                    sort($nums);
                    $k++;
                    if(isset($nums[$middle+1]) && $nums[$middle+1] == $val)
                    {
                        $middle += 1;
                    }
                    elseif(isset($nums[$middle-1]) && $nums[$middle-1] == $val)
                    {
                        $middle -= 1;
                    }
                }
                return(count($nums) - $k);
            }
            elseif($val > $nums[$middle])
            {
                $left = $middle + 1;
            }
            else
            {
                $right = $middle - 1;
            }
        }
        
    }
}