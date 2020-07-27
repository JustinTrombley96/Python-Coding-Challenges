class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # 13/18 Tests Passed

        # if len(nums) >= 2:
        #     for num in nums:
        #         for n in nums:
        #             if num is not None and n == num:
        #                 return True
                
        # All 18 tests pass
        # Runtime: 116 ms
        # Memory: 19.2 MB
        if len(set(nums)) < len(nums):
            return True