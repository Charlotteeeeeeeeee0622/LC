import collections

if __name__ == '__main__':
    def largestPalindromic( num: str) -> str:
        cn = collections.Counter(num)
        cc = sorted(cn.items(), key=lambda x: x[0], reverse=True)  # key 从大到小
        res = []
        for c, freq in cc:
            # if freq % 2 == 0:
            if freq>1:
                # mid=len(res)//2
                # res.insert(mid,c)
                while freq-1:
                    mid = len(res) // 2
                    res.insert(mid, c)
                    freq -= 1
                    print(res)
            # else:
            #     continue

        # for c, freq in cc:
        #     if freq % 2 == 1:
        #         mid = len(res) // 2
        #         res.insert(mid, c)
        #         # res.append(c)
        #         print(res)
                if res[0] != '0':
                    return ''.join(res)
                elif res[0]=='0':
                    # Remove both
                    while res[0] == '0': res = res[1:]
                    while res[-1] == "0": res = res[:-1]
                    return ''.join(res)

    print(largestPalindromic("00001105"))





