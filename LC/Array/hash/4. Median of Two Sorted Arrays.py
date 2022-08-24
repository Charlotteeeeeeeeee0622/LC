class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        left = (m + n + 1) // 2     # 左取整
        right = (m + n + 2) // 2    # 左取整
        # 将偶数和奇数的情况合并,如果是奇数,会求两次同样的k
        return 0.5*( self.get_kth_smallest(nums1, 0, n - 1, nums2, 0, m - 1, left) + self.get_kth_smallest(nums1, 0, n - 1, nums2, 0, m - 1, right) )

    def get_kth_smallest(self, nums1, start1, end1, nums2, start2, end2, k):
        # len表示当前数组，或者经过递归排除过后的数组，符合当前条件的元素的个数
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        # 让len1的长度小于len2,这样就能保证如果有数组空了就一定是 len1
        if len1 > len2:
            return self.get_kth_smallest(nums2, start2, end2, nums1, start1, end1, k)
        # 如果一个数组中没有了元素，那么从剩余数组nums2的起始start2开始再k-1
        if len1 == 0:
            return nums2[start2 + k - 1]
        # 如果k=1，表明最接近中位数了，即两个数组中start索引处，谁的值小，中位数就是谁(start索引之前表示经过迭代已经被排出的不合格的元素，即数组没被抛弃的逻辑上的范围是nums[start]--->nums[end])。
        if k == 1:
            return min(nums1[start1], nums2[start2])
        # 为了防止数组长度小于k//2， 每次比较都会从当前数组的深度与k//2作比较，取其中的小的，防止越界
        # 数组中如果len1小于k//2，表示数组经过下一次遍历就回到末尾，然后就会在那个剩余的数组中寻找
        i = start1 + min(len1, k // 2) - 1
        j = start2 + min(len2, k // 2) - 1

        # nums1[i]>nums2[j]，表示nums2数组中包含j索引，之前的元素，逻辑上全淘汰，即下次从j+1开始
        # 而k变成k-(k-start2+1)，即减去逻辑上排出的元素的个数（要加1，索引相减）
        if nums1[i] > nums2[j]:
            return self.get_kth_smallest(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1))
        else:
            return self.get_kth_smallest(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1))
