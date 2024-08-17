<?php
/**
 * Definition for a singly-linked list.
 * runtime 36ms, beats 40.74%, memory beats 18.87%
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */

 class Solution {
    /**
     * @param ListNode $headA
     * @param ListNode $headB
     * @return ListNode
     */
    function getIntersectionNode($headA, $headB) {
        $ca = $headA;
        $cb = $headB;
        $va = [];
        while($ca != null)
        {
            $va[spl_object_hash($ca)] = true; // add the hash of the object to an array
            $ca = $ca->next;
        }
        while($cb != null)
        {  
            if(isset($va[spl_object_hash($cb)])) // check for the same hash
            {
                return $cb;
            }
            $cb = $cb->next;
        }
        return false; // not found
    }
}