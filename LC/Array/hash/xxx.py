import collections
from typing import List

if __name__ == '__main__':
    def compress(chars: List[str]) -> int:
        res = []
        c = collections.Counter(chars)
        for key, freq in c.items():
            res.append(key)
            for digit in str(freq):
                res.append(digit)
        return res

    print(compress(["a","a","b","b","c","c","c"]))
