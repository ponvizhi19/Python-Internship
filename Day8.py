# Python-Internship
#1
From math import cube
import cube
stud={1:'aaa',2:'bbb',3:'ccc'}
Print(stud(4))

L=[80,54,93]
Print(L[3])

marks=max(L)
if marks<40:
 div=marks/0
 Print(div)
Elif marks>40|marks<80:
 div=marks/2
 print(div)
Else:
 div=marks
 print(div)

Print(name)
age=2
print('age'+2)


#2
def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def mul(a,b):
    c=a*b
    print(c)
def div(a,b):
   try:
    c=a/b
    print(c)
   except Exception as e:
       print("Exception caused:",e)


def enterinput():
    try:
        num1=int(input())
        num2=int(input())
        operator=input()
        if operator=='+':
           add(num1,num2)
        elif operator=='-':
            sub(num1,num2)
        elif operator == '*':
          mul(num1, num2)
        elif operator == '/':
             div(num1, num2)
        else:
              print("wrong input")
              enterinput()
    except Exception as e:
        print("Exception raised :",e)
    finally:
        enterinput()
enterinput()


#3
try:
  a=5
  b=2
  sum=a+b
  print(sum)
  print(name,sum)
except NameError as ne:
  print("name error is caused",ne)
except Exception as e:
  print(e)


#4
Try-except is not required when there is no runtime error


#5
try:
    lst=[]
    n=int(input("Enter n:"))
    for i in range (0,n):
       value=int(input())
       lst.append(value)
    print(lst)
    print("enter index to be popped:")
    pop_ind=int(input())
    lst.pop(pop_ind)
    print(lst)
except Exception as e:
    print(e)
