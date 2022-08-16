def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        if nums[i] > 0:
            break
        # 查重
        if i >= 1 and nums[i] == nums[i - 1]:
            continue
        while left < right:
            if nums[left] + nums[i] + nums[right] > 0:
                right -= 1
            elif nums[left] + nums[i] + nums[right] < 0:
                left += 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left != right and nums[left + 1] == nums[left]: left += 1
                while left != right and nums[right - 1] == nums[right]: right -= 1
                left += 1
                right -= 1

    return res