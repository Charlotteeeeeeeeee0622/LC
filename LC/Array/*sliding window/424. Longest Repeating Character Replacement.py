# ——————————————Solution1————————————————
def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    freq = {}
    maxlen = 0

    for r in range(len(s)):
        # If a character is not in the frequency dict, this inserts it with a value of 1 (get returns 0, then we add 1).
        # If a character is in the dict, we simply add one.
        freq[s[r]] = freq.get(s[r], 0) + 1
        # The key point is that we only care about the MAXIMUM of the seen values.
        # Get the length of the current substring, then subtract the MAXIMUM frequency. See if this is <= K for validity.
        curlen = r - l + 1

        if curlen - max(freq.values()) <= k:
            maxlen = max(curlen, maxlen)
        else:
            # if we have replaced > K letters, then it's time to slide the window
            freq[s[l]] -= 1
            l += 1

    return maxlen

# ——————————————Solution2————————————————
def characterReplacement(self, s, k):
    maxf = i = 0
    count = collections.Counter()
    for j in range(len(s)):
        count[s[j]] += 1
        maxf = max(maxf, count[s[j]])
        if j - i + 1 > maxf + k:
            count[s[i]] -= 1
            i += 1
    return len(s) - i