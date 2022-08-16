class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a = [ord(x) - ord('a') for x in s1]
        b = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for i in a:
            target[i] += 1

        window = [0] * 26

        # for i in range(len(b)):
        for i, x in enumerate(b):
            window[x] += 1
            if i >= len(a):
                window[b[i - len(a)]] -= 1

            if target == window:
                return True
