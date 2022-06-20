# Maximum Subarray
### Difficulty: Easy

Given an integer array **_nums_**, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A **subarray** is a **contiguous** part of an array.

#### Example 1

    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: [4,-1,2,1] has the largest sum = 6

#### Example 2

    Input: nums = [5,4,-1,7,8]
    Output: 23
    
#### Constraints 
- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104


## My Reasoning and Method

From what i've learnt online and from other resources, this problem is solved using the Kamade's algorithm
It is implemented as follows, follow my code to understand properly.

- First we initialise the maximumSum, _**maxSum**_ to the first value of the list. This will enables use to return a 
correct value for an array consisting of just one item.
- Next we set the _**currentSum**_ to 0. The significance of this value will be explained later.
- Iterate through all the values in the list from the front.
  - The value of the first item is added to _**currentSum**_ and it's sum is compared to _**maxSum**_. If it is greater than the _**maxSum**_,
   then _**maxSum**_ value is changed to _**currentSum**_. Another test is conducted to determine the value of _**currentSum**_, if it is less than it's initial value, _**currentSum**_ is reset to 0. 
  This is why we initialised _**currentSum**_ to 0 in the beginning. 0 is neutral to addition (where positive or negative numbers).
 - We then return _**maxSum**_ after all the iterations.
 - Since we don't perform any expensive operations on the list, and the iteration is carried out twice, the algorithm runs in 0(n) time complexity.
  

