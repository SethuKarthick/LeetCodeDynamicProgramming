class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        

        def gcd(a, b):
            while b:
                a, b = b, a%b
            
            return a 

        def lcd(a, b):
            return (a*b) // gcd(a,b)

        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) >= 2:
                a = stack[-2]
                b = stack[-1]
                g = gcd(a, b)
                if g == 1:
                    break 
                stack.pop()
                stack.pop()
                stack.append(lcm(a, b))
        return stack 