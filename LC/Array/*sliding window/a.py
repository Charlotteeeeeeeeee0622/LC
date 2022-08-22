import collections

if __name__ == '__main__':


    def solution(A):
        # write your code in Python 3.6
        nsum = []
        for i in range(len(A)):
            if i < len(A) - 1:
                nsum.append(A(i) + A(i + 1))
        n = collections.Counter(nsum)
        print(nsum)
        #print(n)

    solution([2,3,4,4,5,6])