/**
 * https://leetcode.com/problems/number-complement/?envType=daily-question&envId=2024-08-22
 * @param {number} num
 * @return {number}
 */
var findComplement = function(num) {
    bin = num.toString(2)
    return parseInt(bin.toString().split('').map(n => 1 - n).join(''), 2)
};

console.log(findComplement(5))