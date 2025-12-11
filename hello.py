thislist = ["apple", "banana", "cherry"]
print(thislist)



my_list=["king kong","sachin","dhoni","pavan"]
my_list[1]= "kohli"
print(my_list)

my_list=["vannila","strawberry","BLACK CURRENT"]
my_list[1:3]= "butter scotch","icecreame"
print(my_list)


thislist = ["apple","banana","cherry"]
thislist.append("orange")
print(thislist)

this_list=["pavan","ramu","abhiram"]
thislist.append("Bhargav")
print(this_list)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
    
    
my_dict = {
    "college name":"Gitam University",
    "Stream":"B.tech cse",
    "regd no":"VU21CSEN0101563", 
    "Passed out year":"2025"
}

thislist = ["apple", "banana", "cherry"]
print(thislist)        



num = int(input("enter a number"))

if num %2 == 0:
        print("the number is even")
else:
    print("the number is odd")
        


num= int(input("enter a number"))
 
if num %2 == 0:
   print("the number  is  even")
else:
    print("the number is odd")
    
    
# Program to check even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")    
    
    
num = int(input("enter a number:"))
   
if num %2 == 0:
    print("the number is even")
else:
    print("the number is odd")
       
       
num = int(input("enter a number:"))

if num %2 == 0:
    print("the number is even")
else:
    print("the number is odd")
    
num = int(input("enter a number:"))

if  num %2 == 0:
    print("the number is even")
else:
    print("the number is odd")


num = int(input("Enter a number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")

#palindome
num = int(input("Enter a number: "))
temp = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if temp == rev:
    print("Palindrome number")
else:
    print("Not a palindrome number")
    
num = int(input("enter a number:"))
temp = num
rev = 0

while num > 0:
    digit = num %10
    rev =rev *10 + digit
    num = num // 10
    
if temp == rev:
    print("palindrome number")
else:
    print("not a palindrome number")
    

num = int(input("enter a number:"))
temp = num
rev = 0

while num > 0:
    digit = num %10
    rev=rev*10 + digit
    num = num //10

if temp == rev:
    print("palindrome number")
else:
    print("not a palindrome number")
    
    
num = int(input("enter a number:"))
temp = num
rev = 0

while num > 0:
    digit = num %10
    rev=rev*10  +digit
    num = num //10
    
if temp == rev:
    print("palindrome number")
else:
    print("not a plindrome")
    

num =int(input("enter a number"))
if num%2 == 0:
    print(" even")
else:
    print(" odd")
    
num =int(input("enter a number"))
if num%2 == 0:
    print("even")
else:
    print("odd")
    


num = int(input("enter a number"))
if num%2 ==0:
    print("even")
else:
    print("odd")


    
num = int(input("enter a number"))
if num%2==0:
    print("even")
else:
    print("odd")
    
    
    
my_list=["kohli","Dhoni","sachin"]
my_list.append("Bhuvneswar")
print(my_list)

my_list=["mac book air","iphone13promax","iphone14plus"]
my_list.remove("mac book air")
print(my_list)

my_list=["apple","Banana","cherry","watermelon"]
my_list.insert(1,"cherry")
print(my_list)

my_list=["apple","Banana","cherry","jackfruit"]
my_list.pop(0)
print(my_list)

my_list=[55,858,884,74849,9947,8576,858]
my_list.sort()
print(my_list)


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


my_list=["apple","banana","dragonfruit","beetroot","ladiesfinger","ecofriendly"]
my_list.pop("banana")
print(my_list)

my_dict = {
     "name":"scorpio",
     "Brand":"mahinra",
     "manifacture":"2025",
     "geartype":"automatic",
     "airbags":"six"
}
print(my_dict["Brand"])



my_dict = {
    "Name":"Rohith",
    "college":"Gitam",
    "stream":"B.tech",
    "Branch":"cse",         
}
my_dict.update({"Branch":"computer sceince"})
print(my_dict)


my_dict = {
    "Name":"Rohith.B",
    "date of Birth":"2001",
    "regd no":"VU21CSEN0101563",
    "Block":"ICT",
    "Branch":"cse"
}
my_dict["year"] = 2002
print(my_dict)


my_dict = {
     "Name":"Rohith.B",
    "date of Birth":"2001",
    "regd no":"VU21CSEN0101563",
}
my_dict.update({"colour":"red"})
print(my_dict)


my_dict = {
    "model":"2025",
    "year":"2024",
    "manifacturing":"toyato",
    "Build quality":"strong", 
}
my_dict.pop("model")
print(my_dict)


my_dict = {
    "Platfrom":"amazon",
    "unit sold":2,
    "cost per piece":1200,
}
for x in my_dict.values():
    print(x)
    
    
    
my_dict ={
    "dress type":"shirt",
    "hsn code":"1232",
    "company":"super sauda",
    "trade unit":26    
}
my_dict=my_dict.copy()
print(my_dict)

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


a= 77
b=80

if a>b:
    print("a is greater")
elif a==b:
    print("a equals to b ")
else:
    print("b is greater than a")
    
    
    
x= 40

if x>40:
    print("x is equal")
elif x != 40:
    print("x is not equal to 40")
else:
    print("x is not at all equal")    
    
    


a= float(input("enter first number:"))
b= float(input("enter a second number:"))

if a > b:
    print("Maximum is a")
elif  b>a:
    print("maximum is b")
else:
    print("Both are equal")


a=float(input("enter  first number"))
b=float(input("enter a second number"))
c=float(input("enter a third number:"))

if  a>b:
    print("maximum is a")
elif b>a:
    print("maximum is b")
elif c<a:
    print("maximum is c")
    
else:
    print("all are not equal")
    
 ####   
n= float(input("enter a number"))

if n >0:
    print("positive")
elif n <0:
    print("negative")
else:
    print("zero")
    
#####3
n = int(input("Enter a number: "))

if n % 5 == 0 and n % 11 == 0:
    print("Divisible by both 5 and 11")
else:
    print("Not divisible by 5 and 11 ")



#####
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#######
n = int(input("enter a number"))

if n % 2 ==0:
    print("even")
else:
    print("odd")
    
n = int(input("enter s fisrt number"))
if n %2 ==0:
    print("even")
else:
    print("odd")
    
 ##########3   
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
    
year = int(input("enter a year"))

if (year % 400 ==0) or (year %4 ==0  and year %100 !=0):
    print("leap year")
else:
    print("not a leap year")

#######
year = int(input("enter a year"))

if (year %400 ==0) or (year %4 ==0 and year %100 !=0):
    print("leap year")
else:
    print("not a leap year")

######
s = input("Enter a sentence: ")
words = s.split()      
words.reverse()        

result = " ".join(words)
print(result)

######
s = input("Enter a sentence: ")
words = s.split()      
words.reverse()        

result = " ".join(words)
print(result)

####
R = input("entert a word")
words = R.split()
words.reverse()

result = " ".join(words)
print(result)

s = "python programming"
words = s.split()
result = []

for w in words:
    result.append(w[::-1])

print(" ".join(result))

##second assignmet
r = "Python programming"
words = r.split()
result = []

for w in words:
    result.append(w[::-1])
print(" ".join(result))

#######
s1 = "teja"
s2 = "sri"
result = ""
i = 0

while i < len(s1) or i < len(s2):
    if i < len(s1):
        result += s1[i]
    if i < len(s2):
        result += s2[i]
    i += 1

print(result)

#################
s1 = "rohith"
s2 = "bonthu"
result = ""
i = 0

while i < len(s1) or i < len(s2):
    if i < len(s1):
        result += s1[i]
    if i < len (s2):
        result += s2[i]
    i += 1
################    
s1 = "rohith"
s2 = "bonthu"
result = ""
i = 0
while i <len(s1) or i < len(s2):
    if i < len(s1):
        result += s1[i]
    if i < len (s2):
        result += s2 [i]
    i += 1 
    
################
s1 = "bonthu"
s2 ="rohith"
result = ""
i  = 0
while i <len(s1) or i <len(s2):
    if i < len(s1):
        result += s1[i]
    if i < len (s2):
        result += s2 [i]
    i += 1
    
    ########
    
    s = "B4A1D3"
letters = []
numbers = []

for ch in s:
    if ch.isalpha():
        letters.append(ch)
    else:
        numbers.append(ch)

letters.sort()
numbers.sort()

print("".join(letters + numbers))


##############3
s="Rad368"

letters = []
numbers = []

for ch in s:
    if ch.isalpha():
        letters.append(ch)
    else:
        numbers.append(ch)
    
    letters.sort()
    numbers.sort()
print("".join(letters + numbers))

#####

s="64ggftd"

letters = []
numbers = []

for ch in s:
    if ch.isalpha():
        letters.append(ch)
    else:
        numbers.append(ch)
    
    letters.sort()
    numbers.sort()
print(".join(letters+numbers)")

#########33
s = "a4b3c2"
result = ""

for i in range(0, len(s), 2):
    letter = s[i]
    num = int(s[i+1])
    result += letter * num

print(result)

###########

s = "534fdedrr5"
result = ""

for i in range(0,len(s),2):
    letter = s[i]
    num = int(s[i+1])
    result += letter *num
    
print(result)

########

s = "63t47tgget"
result = ""

for i in range(0,len(s),2):
    letter = s[i]
    num = int(s[i+1])
    result += letter *num

print(result)


###########

s = "ABCDABBCDEEFFG"
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)


#####################3
s="AABBDJJIJJDJJBDKLW"
result = ""

for py in s:    
    if   py  not in result:
        result += py

print(result) 
        
######################
        
list = [1,2,3,4,5]
total = 0

for x in list:
    total += x

print(total)


list = [1,2,3,4,5]
total = 0

for x in list:
    total += x

print(total)
    


list = [0,873,727,2,4,4]
total=0

for x in list:
    total += x
    
print(total)



s = "ABCABCABBCDE"

for py in s:
    if py not in s[:s.index(py)]:
        print(py, "-", s.count(py))
        

s = "ANDKIDJKEE"
 
for py in s:
    if py not in s[:s.index(py)]:
  
      print(py, "-", s.count(py))
  
   ## 
lst = [7,8,120,25,44,20,27]
new = []

for x in lst:
    if x % 2 != 0:
        new.append(x)

print(new)

####
list = [7,8,120,25,44,20,27]
new = []

for x in list:
    if x % 2 != 0:
        new.append(x)

print(new) 
####
i = 1 
while True:
    print(i)
    i += 1

chars = ['a','b','c','d']
print("".join(chars))



###

result = []

for i in range(1, 21, 5):
    group = [i, i+1, i+2, i+3, i+4]
    result.append(group)

print(result)

##infinite loop
i = 1
while True:
    print(i)
    i += 1
    
    
    ###
    
    lst = [3,5,7,13]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

all_prime = True

for x in lst:
    if not is_prime(x):
        all_prime = False
        break

print(all_prime)

    
    
    
