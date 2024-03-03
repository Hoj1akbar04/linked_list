class Solution:
    @staticmethod
    def palindrome(x: int) -> bool:
        if x < 0:
            return False
        p = 1
        while x >= 10 * p:
            p *= 10

        while x:
            if x // p != x % 10:
                return False
            x = (x % p) // 10
            p = p / 100
        return True


solution = Solution()
print(solution.palindrome(121))
print(solution.palindrome(-121))
print(solution.palindrome(10))


"""def palindrome(x):
    a = str(x)
    return a == a[::-1]


x = 12321
print(palindrome(x))

x = -121
print(palindrome(x))

x = 10
print(palindrome(x))"""






