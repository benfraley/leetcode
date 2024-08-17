<?php
/**
 * https://leetcode.com/problems/linked-list-cycle-ii/
 * runtime 13ms, beats 62.5%, memeroy beats 87.5%
 * learned a bit from the previous linked_list_cycle.php and implemeneted
 * a slow/fast pointer solution
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */

class Solution {
    /**
     * @param ListNode $head
     * @return ListNode
     */
    function detectCycle($head) {
        $slow_pointer = $head;
        $fast_pointer = $head;
        while($fast_pointer != null && $fast_pointer->next != null)
        {
            $slow_pointer = $slow_pointer->next; // this one runs slow
            $fast_pointer = $fast_pointer->next->next; // this one runs fast
            if($slow_pointer == $fast_pointer) // if they meet we have a loop
            {
                $slow_pointer = $head; // need to find where they met
                while ($slow_pointer != $fast_pointer)
                {
                    $slow_pointer = $slow_pointer->next;
                    $fast_pointer = $fast_pointer->next;
                }
                return $slow_pointer; // this is where they met
            }
        }
        return null;
    }
}