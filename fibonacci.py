# 1,1,2,3,5,,8,13,..... , n

# a = 0
# b = 1
# temp = 1
# num = 10
# for i in range(1,num + 1):
#     print(f"{temp},",end = " ")
#     temp = a+b
#     a = b
#     b = temp
    
class solution:
    def func(self,num):
        if num == 0 or num == 1:
            return num
        return  self.func(num - 1) + self.func(num - 2)

    def fibonacci(self,num):
        num = int(num)
        return self.func(num)

sol = solution()
print(sol.fibonacci(6))