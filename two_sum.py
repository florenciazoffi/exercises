# Leetcode
"""
Instructions:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""

# Uses brute force to check if the sum of two numers in the nums list is equal to the target
class Brute_Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        l_nums = len(nums)
        for i in range(l_nums - 1):
            for j in range(i + 1, l_nums):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Uses a dictionary to store elements and their indices, calculates the compliments of the numbers in the nums list to find a solution
class Dict_Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        l_nums = len(nums)

        # Creates the dictionary with each number and its index
        for i in range(l_nums):
            num_dict[nums[i]] = i
        
        # Calculate the missing number for each element and checks if it's in the dictionary created before
        for i in range(l_nums):
            missing = target - nums[i]
            if missing in num_dict and num_dict[missing] != i:
                return [i, num_dict[missing]]

# Shorter, more efficient solution (dict_solution)
class Short_Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        num_dict = {}
        l_nums = len(nums)

        for i in range(l_nums):
            missing = target - nums[i]
            if missing in num_dict and num_dict[missing] != i:
                return [i, num_dict[missing]]
            num_dict[nums[i]] = i

def main():
    num_list = [2,7,11,15]
    b_solution = Brute_Solution()
    d_solution = Dict_Solution()
    s_solution = Short_Solution()
    print(b_solution.two_sum(num_list, 9))
    print(d_solution.two_sum(num_list, 9))
    print(s_solution.two_sum(num_list, 9))

if __name__ == "__main__":
    main()