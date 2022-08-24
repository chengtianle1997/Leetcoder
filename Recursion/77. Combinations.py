class Solution:
    
    def generate(self, path, start, n, k):
        if k == 0:
            self.res.append(path)
        for i in range(start, n + 1, 1):
            if k > 0:
                self.generate(path + [i], i + 1, n, k - 1)
            else:
                return
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.generate([], 1, n, k)
        return self.res
        
        