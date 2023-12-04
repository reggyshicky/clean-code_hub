//Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 function squaresofassortedarray(nums) {
    result = nums.map((x) => x * x)
    return result.sort(function(a, b) {return a - b})
 }

 console.log(squaresofassortedarray([-4,-1,0,3,10]))