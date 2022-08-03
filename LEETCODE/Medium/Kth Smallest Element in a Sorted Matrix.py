class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 기본적인 모듈들은 다 내장되어있는듯 하다.
        return sorted(list(itertools.chain(*matrix)))[k-1]