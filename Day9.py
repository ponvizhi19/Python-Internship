# Python-Internship
#1
a=lambda x,y: x*y
print(a(13,9))

#2
from functools import reduce
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1])
print(fib(9))

#3
nums = [1,2,3,4,5,6,7,8,9,10]
n=int(input("enter the num to be multiplied with:"))
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))

#4
my_list = [12, 65, 54, 39, 102, 339, 999]
result = list(filter(lambda x: (x % 9 == 0), my_list))
print("Numbers divisible by 9 are",result)

#5
nums = [1, 2, 3, 156, 7, 8, 12, 10]
print("Original arrays:")
print(nums)
even = len(list(filter(lambda x: (x%2 == 0) , nums)))
print("\nNumber of even numbers in the above array: ", even)
