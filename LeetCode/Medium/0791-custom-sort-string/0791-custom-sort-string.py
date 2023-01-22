class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order = list(order)
        for i in range(len(order) - 1, -1, -1):
            cnt = s.count(order[i])
            s = order[i] * cnt + s.replace(order[i], '')
        return s