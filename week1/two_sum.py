class Solution:
    # Brute-force method
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i, n in enumerate(nums):
    #         for j, m in enumerate(nums):
    #             if i != j and n == target - m:
    #                 return [i, j]
    
    # One-pass dictionary method
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp in comps and comps[comp] != i:
                return [i, comps[comp]]
            comps[n] = i