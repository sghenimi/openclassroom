import math
class AllPrimeNumbers:
    def countPrimes(self, n):
        if n < 3:
            return 0

        arr = [0] * n
        arr[0] = 1
        arr[1] = 1
        sqrt = int(math.sqrt(n))
        for i in range(2, sqrt + 1):
            j = 2
            while (i * j) < n:
                arr[i * j] = 1
                j += 1

        return len([num for num in arr if num == 0])

    def mySqrt(self, x: int) -> int:
        x = x ** (1 / 2)
        z = math.floor(x)
        return z