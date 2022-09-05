class Solution:
    
    def generate(self, s, left, right):
        if left == 0 and right == 0:
            # find a result
            self.res.append(s)
        if left > 0:
            self.generate(s + '(', left - 1, right)
        if right > 0 and right > left:  # the right need to be paired with left
            self.generate(s + ')', left, right - 1)
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.generate("", n, n)
        return self.res
        