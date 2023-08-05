class Solution(object):


    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def factorial(n):
        
            fact = 1
            for i in range(1, n+1):
                fact = fact * i

            return fact

        def get_variants(number):
            
            res = []
            
            for i in range(0, number):

                if number - 2 * i >= 0:
                    res.append((number - i, i))
                else:
                    break
             
            return res

        variants = get_variants(n)
        results = 0
        
        for n, k in variants:
            results += factorial(n)/factorial(n - k)
        
        return results

        

sol =  Solution()
# print(sol.climbStairs(0))
print(sol.climbStairs(4))     

## fgggfddfghb

        


