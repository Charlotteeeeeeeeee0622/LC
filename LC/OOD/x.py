if __name__ == '__main__':

    def findSubarrays(nums):
        def backtracking(nums, path):
            if len(path) == 2:
                res.append(sum(path))
                return

            for i in range(len(nums)):
                backtracking(nums[i + 1:], path + [nums[i]])

        res = []
        backtracking(nums, [])

        return not len(res)==len(set(res))
    #findSubarrays([1,2,3,4,5])


    def findSubarrays1(nums):
        l = 0;
        r = 0;
        w = [];
        res = []
        while r <len(nums) :
            if len(w) == 2:
                res.append(sum(w))
                del w[l]
            w.append(nums[r])
            r += 1
        if len(w)==2:
            res.append(sum(w))
        return len(res) == len(set(res))
    findSubarrays1([4,2,4])