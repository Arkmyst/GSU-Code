class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1:
            return 1

        trust_counter = [0] * (n + 1)
        trusted_counter = [0] * (n + 1)

        for a, b in trust:
            trust_counter[b] += 1
            trusted_counter[a] += 1

        for i in range(1, n + 1):
            if trust_counter[i] == n - 1 and trusted_counter[i] == 0:
                return i

        return -1
