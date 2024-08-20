/**
 * https://leetcode.com/problems/symmetric-tree/
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    let level = []; // creating an array of levels to compare
    curLevel = 0; // the level we're at now
    level = traverse(root, level, curLevel); // recursively get all the levels

    let sym = true;
    level.forEach(function(l){
        rl = l.slice().reverse()
        // if the array is the same as its reverse, it's symmetric
        if(JSON.stringify(l) !== JSON.stringify(rl))
        {
            sym = false
            return
        } 
    })

    if(sym !== false)
    {
        return true
    }
    else
    {
        return false
    }
    
};

var traverse = function(root, level, curLevel) 
{
    // stop on null roots
    if(root === null)
    {
        return level;
    }

    // initialize
    if(level[curLevel] === undefined)
    {
        level[curLevel] = [];
    }
    // add the right and left vals to the current level array
    level[curLevel].push(root.left ? root.left.val : null);
    level[curLevel].push(root.right ? root.right.val : null);
    // traverse the right and left trees, increasing their levels
    traverse(root.left, level, curLevel+1);
    traverse(root.right, level, curLevel+1);
    return level;
}