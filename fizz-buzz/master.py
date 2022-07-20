class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        statues  = ["FizzBuzz", "Fizz", "Buzz"]
        result = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0 and i != 0:
                result.append(statues[0])
            elif i % 3 == 0 and i != 0:
                result.append(statues[1])
            elif i % 5 == 0 and i != 0:
                result.append(statues[2])
            else:
                result.append(str(i))
        
        return result


print(Solution().fizzBuzz(3))
