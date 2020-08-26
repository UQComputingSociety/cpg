class Solution:
    # To climb to step i, you can do two things:
    # - climb 1 from step i - 1
    # - climb 2 from step i - 2
    # So just add the sum of the possibilities up to i - 1
    # and the sum of the possibilities up to i - 2
    # This reduces to the Fibonacci sequence.
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.memo(n)
        
    def memo(self, n: int) -> int:
        cache = {1: 1, 2: 2}
        
        for i in range(2, n+1):
            cache[i+1] = cache[i] + cache[i-1]
        
        return cache[n]