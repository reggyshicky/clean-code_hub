//This approach is used with a sorted array

function TwoSumTarget(arr, target) {
    let left = 0;
    let right = arr.length - 1;

    while (left < right) {
        let currentSum = arr[left] + arr[right]
        if (currentSum == target) {
            return true;
        } else if (currentSum < target) {
            left++;
        } else {
            right--;
        }
    }
    return false;
}

console.log(TwoSumTarget([1,2,3,4,5], 5));
console.log(TwoSumTarget([1,2,3,4,5], 50));