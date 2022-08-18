def my_fun():
    print("Hello")

my_fun()

def mufun():
    pass
print("hey you")

def my_fuction(name):
    print(f"hello {name}")

my_fuction("akshata")

def myfunc(fname,lname):
    print(f"Hi {fname} {lname}")

myfunc("Akshata", "Kolli")

a=100
def num():
    print(a)
num()

a=100
def num_():
    b=a+1
    print(b)
num_()

a=100
def number():
    global a
    a+=10
    print(a)
number()

print(a)

a=40
b=30
# def sum3():
#     sum3=a+b
#     print(sum3)
# sum3()
# print(a, b)
# print(sum3)
#
# a=40
# b=30
# total_sum=0
# def sum():
#     total_sum=a+b
#     print(total_sum)
# sum()
# print(total_sum)
#
# a=40
# b=30
# total_sum=0
# def sum():
#     global sum
#     total_sum=a+b
#     print(total_sum)
# sum()
# print(total_sum)
#
# def sum2(a, b):
#     print(a+b)
# sum2(10,20)
# sum2(200, 50)
#
# def sum1(a=0,b=0):
#     print(a+b)
# sum1()
# sum1(30)
# sum1(10+20)
# sum1(b=20)

def sum1(a, b=0):
    print(a+b)
sum1(30)

# def sum(a=0, b):
#     print(a+b)
# sum(30)


def even(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
even(2)
print(type(num))
print(type(even))

ml=[5,6,7,8]
ml.clear()
print(ml)

ml = [1,2,3,4,5,6,7,8]
print(sum(ml))

# def jodi(seq):
#     global total_sum
#     for i in seq:
#         total_sum+=i
#     print("nnn" ,total_sum)

# jodi([2,3,4,5,6,7,8])
#
# def join(seq):
#     total_sum=0
#     for i in seq:
#         total_sum += i
#     print("aks,total_sum")
#
# join(3,5,7,9,2,4,6)

def join1(*seq):
    total_sum = 0
    for i in seq:
        total_sum += i
    print(total_sum)

join1(3,4,8,6)

# def printname(**person):
#     print(f"The name of person is {person['name']}, and her age is {person['age']}")
# printname(name="Akshata", age=26, subject="python")
#
# person={'name':'Akshata','age': 28,'subject':'python'}
# print(person)
# print(person['name'])
#
# def printname(*numbers,**person):
#
#     print(person["name"])
#     print(numbers)
#
# printname(30,40,50,name='Akshata',age=40,subject='Python')

# def printname(**person,*numbers):# we cann't put multiple arguments parameter as last parameter of the function
#
#     print(person['name'])
#     print(nambers)
# printname(name="Akshata", age=34, 'subject'='python')

for i in range(1,5):
    print('?????'*i)

for i in range(1,11):
    if i==1 or i==10:
        print('?????'*10)
    else:
        print('?????','?????',sep='?????'*8)


# def code():
#     print('python')
# code()
#
# a=code()
# print(a)
# print('------------------')
# def code(n):
#     return (n)
# n='radhe'
# a = code(n)
# print("is it a print ",a)
# #
# def fibb(a=0,b=1,num=8):
#     print(a)
#     print(b)
#     for i in range(num):
#         temp=a+b
#         a  = b
#         b= temp
#         print(temp)
# fibb(11,12,5)
#
# def sumof(nums):
#     temp=1
#     for i in nums():
#         temp*=i
#     print(temp)
# sumof([10,11,12])

num=490
multiple=[]
for i in range(1,num):
    if num % i == 0:
        multiple.append(i)
print(multiple)
print(sum(multiple))

def perfectnum(num):
    multiple=[]
    for i in range(1,num):
        if num % i==0:
            multiple.append(i)
    if sum(multiple)==num:
        return 'perfect num'
    else:
        return 'not perfect num'
a=perfectnum(int(input("enter the num:")))
print(a)

def perfect_num(num):
    multiple=[]
    i=num-1
    while i > 0:
        if num % i==0:
            multiple.append(i)
        i-=1
    return multiple
perfect_num(4)

def sumofigit(num):
    total_sum=0
    while num>0:
        r=num%10
        total_sum+=r
        num//=10
    print(total_sum)
sumofigit(12345)

















