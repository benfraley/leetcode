<?php
// https://leetcode.com/problems/linked-list-cycle/
// runtime 599ms, beat 5.38%, memory 62.37%
// not the most efficient but makes the most sense, intuitively
// saw another solution using two pointers that i will incorporate next time
/**
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
    * @return Boolean
    */
   function hasCycle($head) {
       $current = $head; // for looping
       $prevNodes = array(); // nodes we've already seen

       while($current != null) // looping through the nodes
       {
           if(in_array($current->next, $prevNodes, true)) // if the current is in previous, it's recursion
           {
               return true;
           }
           $prevNodes[] = $current; // add current node to previously seen
           $current = $current->next; // move to next node
       }
       return false; // will only reach here if node not found in prevNodes
   }
}