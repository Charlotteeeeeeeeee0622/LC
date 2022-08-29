class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 记录至今能走到的最远位置(位置均用列表下标表示, 初始化为第一个位置下标 0);
        end = 0
        n = len(nums)
        # 遍历列表位置下标 i, 结合该位置 i 以及从该位置能往后跳的步数 nums[i], 更新当
        # 前能跳到的最远距离 end; 如果遍历到当前位置 i 时, 上一步能跳到的最远距离 end
        # (还没结合当前能跳的最远距离进行更新) 小于当前位置 i, 则说明之前能跳到的最远
        # 距离不能到当前位置 i, 则后续的位置都将无法跳到, 直接返回 False;

        # 遍历时实际上只需要遍历到倒数第二个位置即可, 因为如果能跳到倒数第二个位置(即
        # 下标为 n-2, 只要 nums[n-2] 不为 0, 则就可以往后跳, 此时最后一轮的 end 会更新
        # 为大于或等于 n-1 的值; 最极短的情况下的上一轮只能跳到 n-2 位置, 且 nums[n-2]
        # 的值为 0, 表明从该位置之后不能再继续往后跳了, 此时更新后的 end 也仍然保持在
        # n-2, 最终返回的也是 False); 当然直接循环到最后一个位置也是可以的, 因为如果能
        # 跳到最后一个位置, 则 end 值会基于最后位置 n-1 的基础上结合最后的 nums[n-1] 进
        # 行更新, 尽管后面没有其它位置可跳, 但 end 能执行到该更新逻辑也表明其能到达最后
        # 一个位置了, 否则会在更新 end 之前就返回 False 了;
        for i in range(n-1):
            step = nums[i]
            if i > end:
                return False
            # 基于当前能走的最大步数更新至今能走到的最远位置;
            end = max(end, i + step)

        return end >= n-1

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far = 0
        for i in range(len(nums) - 1):
            step = nums[i]

            if i > far:
                return False

            far = max(far, i + step)

        return far >= len(nums) - 1