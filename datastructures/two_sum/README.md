# Two Sum
### Difficulty: Easy

Given an array of integers __**num**__ and an integer __**target**__, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

#### Example 1

    Input: **__nums__** = [2,7,11,15], __**target**__ = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#### Example 2

    Input: __**nums**__ = [3,2,4], __**target**__ = 6
    Output: [1,2]
    
#### Constraints 
- 2 <= nums.length <= 104
- 109 <= nums[i] <= 109
- 109 <= __**target**__ <= 109
- Only one valid answer exists.


## My Reasoning and Method

I quick to solve this one but it turned out, it was very inefficient with memory even though it saved memory.

- Simply iterate through __**nums**__ with i for the first time.
  - Then iterate through __**nums**__ for the second time with j starting from the second element.
  - The test if nums[i] + nums[j] equals target. If true return [i, j]. 
  
This algorithm has runtime complexity of 0(n^2)

## Even faster algorithm


