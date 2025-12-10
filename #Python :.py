# Python :
# language:it is communication between human and machine
# programming language:it is a set of instructions written in a specific syntax
# to perform a specific task
# low-level,mid-level,high-level
# low-level :where code is expressed in binary or assembly language,
#  closely tied to hardware,it improves  machine efficiency.ex:assembly language
# high-level:where code is expressed in human-readable form,alphabets
# .it improves developer productivity,program efficiciency.ex:python,java,c++
# mid-level:combines elements of both low-level and high-level languages,
# c is mid-level language


# packages:it is a collection of modules that provide specific functionality
# spreadsheet:excel,google sheets
# word processor:ms word,google docs,
# presentation software:ms powerpoint,google slides
# dbms: small amount of data stored in tabular form,ms access,sqlite,files
# rdbs:large amount of data stored in tabular form,mysql,oracle,sql server
# nosql:mongodb

# interpretter vs compiler

# scripting language:it is defined within scripts where
#  instructions are executed line by line
# a=10
#  vs programming language:it is defined within programs
#  where instructions are compiled and executed as a whole 
# python:
# in 1989 by guido van rossum
# 1991 first released
# python1,python2,
# python3.14:latest version
# features:
# code readability and maintainability
# easy to learn and read
# interpreted language
# dynamically typed language
# object-oriented programming language
# cross-platform language
# embedded language:it can be embedded within other languages
# extensive standard library
# it is high-level language
# large community support


# flavours of python:
# jpython:integrated with java,jvm 
# cpython:integrated with c language,c compiler
# ironpython:integrated with .net framework,c#
# rubypython:integrated with ruby language,ruby interpreter
# anaconda python:used for data science and machine learning,when we want to handle large amount of data
# pypy:fast execution of code,just-in-time compiler


# editors/Ides:
# integrated development environment
# pycharm,vscode,ananconda,notepad++,text editor,jupyter notebook

# extensions:
# .py


# architecture of python:
# initialization,condition,print


# built in functions:
# id(),
# a="hello world"
# print(id(a))
#print(),type(),input(),len(),int(),str(),float(),list(),tuple(),set(),dict()
a1=int(input("enter a value:"))
print(a1)
print(type(a1))


#operators:
#arthimatic operators:
# + , - , * , / , % , ** , //
a=10
b=3
print(a+b)  #13
print(a-b)  #7
print(a*b)   #30
print(a/b)   #3.33
print(a%b)   #1
print(a**b)  #1000
print(a//b)  #3  #floor division

#assignment operators:
#=, +=, -=, *=, /=, %=, **=, //=

#sum of numbers 1 to 10

#1+2+3+4+5+6+7+8+9+10
sum=0
for i in range(1,11):
    sum=sum+i     #sum=sum+i   #0=0+1=1+2=3+3=6+4
print(sum)

#product of numbers 1 to 10
#1*2*3*4*5*6*7*8*9*10
product=1
for i in range(1,6):
    product*=i   #product=product*i
print(product)
#comparision operators:
#content comparison with values;if content is true then true else false
#==, !=, >, <, >=, <=
x=5
y=10
print(x==y)   #False
print(x!=y)   #True
print(x>y)    #False
print(x<y)    #True
#logical operators:
#and, or, not
#and operator: true and true = true,true and false = false,false and false = false
#or operator: true or true = true,true or false = true,false or false = false
#not operator: true = false,false = true
a1=23
b1=15
print(a1>b1 or b1>a1)
#not operator:
print(not(a1<b1))

#identity operators:
#is , is not
m="python programming"
print("J" is m)  
print(m is not "python programming")
#memebership operators:
#in , not in
n="welcome to python programming"
print("is" not in n)

#bitwise operators:
#& , | , ^ , ~ , << , >>
#0&1
a2=5
b2=4

print(a2 & b2)
#5 --0 1 0 1
#4----0 1 0 0
#datatypes:
#memory allocation for storing data
#int, float, complex, bool, str, list, tuple, set, dict,frozenset,bytes,bytearray
#int:
x=10
print(type(x))
#float:
y=10.555
print(type(y))
#complex:
a3=10+3j
print(type(a3))
#real and imaginary parts
print(a3.imag)
print(a3.real)
#string
s="""
welcome 
to python
 programming"""
print(type(s))
#list:
list1=[1,2.3,"python",True,5+2j]
print(type(list1))
print(list1)
#tuple:
tuple1=(1,2.3,"python",False,3+4j)
print(type(tuple1))
print(dir(tuple))
#set:
set1={1,2.3,"python",True,5+2j}
print(type(set1))
print(set1)
#frozenset:
#it is immutable version of set, we cannot modify frozenset,it does not support item 
# assignment and item deletion and return a new frozenset
fs=frozenset(set1)
print(type(fs))
print(fs)
#dictionary:
dict1={
    "a":"apple",
    "b":"banana",
}
print(type(dict1))
print(dict1)
#boolean:
boo1=True
print(type(boo1))
#bytes:
bts="python programming"
bts1=bytes(bts, 'utf-8')
print(type(bts1))
print(bts1)
#bytearray:
bta=bytearray(bts, 'utf-8')
print(type(bta))
print(bta)


thislist = ["apple", "banana", "cherry"]
print(thislist)

my_list