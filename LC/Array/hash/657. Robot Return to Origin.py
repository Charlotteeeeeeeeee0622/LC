class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r = 0
        l = 0
        u = 0
        d = 0
        for c in moves:

            if c == 'L':
                l += 1
            elif c == 'R':
                r += 1
            elif c == 'U':
                u += 1
            elif c == 'D':
                d += 1

        if l == r and u == d:
            return True
        else:
            return False


class Solution:
    def judgeCircle(self, moves):
        c = collections.Counter(moves)
        return c['L'] == c['R'] and c['U'] == c['D']