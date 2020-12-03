# Python-Internship
#1
def merge(list1, list2):
    merged_list = tuple(zip(list1, list2))  
    return merged_list 
list1 = [1, 2, 3] 
list2 = ['a', 'b', 'c'] 
print(merge(list1, list2)


#2
l1=["Python", "Internship", "Vel", "Kayal", "Siva", "Kavin", "Ponvizhi"]
r= list(range(1,8))
l=tuple(zip(r,l1))
print(l)


#3
n = [7,13,79,2,68,1]
a=sorted(n)
print(a)


#4
numbers = [1, 2, 4, 5, 7, 8, 10, 11]
def even(in_num):
    if(in_num % 2) !=0:
        return True
    else:
        return False
odd= filter(even, numbers)
print("odd numbers are: ", list(odd))
