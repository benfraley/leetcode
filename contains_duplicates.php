<?php
/**
 * https://leetcode.com/problems/contains-duplicate/
 * runtime 175ms, beats 45.22%, memeory 11.3%
 */
class Solution {

    /**
     * @param Integer[] $nums
     * @return Boolean
     */
    function containsDuplicate($nums) {
        $u = array_unique($nums); // get all unique values
        if(count($nums) == count($u)) return false; // compare, if the same there's no repeats
        return true;
    }
}