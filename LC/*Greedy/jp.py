if __name__ == '__main__':
    def subsum(nums):
        n=len(nums)
        res=0
        for i in range(n):
            res+=nums[i]*(i+1)*(n-i)

        return res

    nums=[4,5,6]
    print(subsum(nums))