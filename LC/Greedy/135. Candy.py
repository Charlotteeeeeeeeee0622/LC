class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) <= 1:
            return len(ratings)

        record = [1] * len(ratings)

        # kids on upwards curve get candies
        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i - 1]:
                record[i] = record[i - 1] + 1

        # kids on downwards curve get candies
        # if a kid on both up/down curves, i.e. a peak or a valley
        # kid gets the maximum candies among the two.

        for i in range(len(ratings), 0, -1):
            if i < len(ratings) and ratings[i - 1] > ratings[i]:
                record[i - 1] = max(record[i] + 1, record[i - 1])
        # for i in range(len(ratings)):
        #     if i>0 and ratings[i]<=ratings[i-1]:
        #         record[i-1]=max(record[i]+1,record[i-1])
        return sum(record)


