# Contains Duplicate
### Difficulty: Easy

Given an integer array _**nums**_, return true if any value appears at _**least twice**_ in the array, 
and return false if every element is distinct.

#### Example 1

    Input: nums = [1,2,3,1]
    Output: true

#### Example 2

    Input: nums = [1,2,3,4]
    Output: false
    
#### Constraints 
1 <= nums.length <= 105
-109 <= nums[i] <= 109


## My Reasoning and Method

My reasoning was straight forward intuitive. I just exploited the property of sets that allows
the just to contains unique values. So a difference between _**nums**_ and a set from nums will prove uniqueness or not.
Time complexity of my solution depends on the implementation of the _**set()**_ function, which is **_0(n)_**
