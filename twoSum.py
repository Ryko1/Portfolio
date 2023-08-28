
class Solution(object):
    def twoSum(self, nums, target):
        self.nums = nums
        self.target = int(target)

        num_to_index = {}  # Dictionary to store numbers and their indices

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                # Return indices of the two numbers
                return [num_to_index[complement], i]
            num_to_index[num] = i  # Store the current number and its index

        return []  # Return an empty list if no solution is found


instance = Solution()

tlist = [2, 7, 11, 15]
target_sum = 18
result = instance.twoSum(tlist, target_sum)

print(result)
