# 给一个长度为n的数组表示n个月的股价，给定k值，给连续k月并且k个值各不一样的区间求和，找到最大和。
# 例子：｛1，2，3，4｝，k=2，那总共有(1,2) (2,3)(3,4)三个长度为k的连续区间并且每个区间没有重复数值，最大和是7。
# ——————————————Solution1————————————————
def max(prices, k):
    w = []
    maxp = -1
    l = 0
    for r in range(len(prices)):
        w.append(prices[r])
        if r >= k:
            l += 1
            w.pop(0)
            if len(set(w)) == k:
                maxp = max(maxp, sum(w))
    return maxp

# ——————————————Solution2————————————————


def max_stock(prices,k):
    maxp=0
    for i in range(len(prices)):
        w=prices[i:i+k]
        if len(set(w))==k:
            maxp=max(maxp,sum(w))
    return maxp

if __name__ == '__main__':
    prices = [1, 2, 3, 4]
    k = 2
    res=max_stock(prices, k)
