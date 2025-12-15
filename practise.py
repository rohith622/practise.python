a=int(input("enter a number"))
b= int(input("enter b number"))
if a>b:
    print("a is greater than b")
elif a==b:
    print("a and b are equal")
else:
    print("b is greater than a")  


#greater three  numbers
a=int(input("enter a number"))     
b= int(input("enter b number"))
c= int(input("enter c number"))
if a>b and a>c:
    print("a is greatest")
elif b>c and b>a:
    print("b is greatest")
else:
    print("c is greatest")    
   
   
    #positive negative zero
a=int(input("enter a number"))
if a>0:
    print("a is positive")
elif a<0:
    print("a is negative")
else:
    print("a is zero")


#divisible by 5 and 11

a=int(input("enter a number"))
if a%5==0 and a%11==0:
    print("a is divisible by 5 and 11")
else:
    print("a is not divisible by 5 and 11")
    
    
    #even odd
a=int(input("enter a number"))
if a%2==0:
    print("a is even")
else:
    print("a is odd")
    

#leap year
a=int(input("enter your number"))
if (a%4==0 and a%100!=0) or (a%400==0):
    print("a is leap year")
else:
    print("a is not leap year") 
    
#alpahabet

a=input("enter a character")

if a.alpha():
    print("a is alphabet")
else:
    print("a is not alphabet")

# vowel or consonant.
a=input("enter a character").lower().split()
b = "aeiou"
if b in a:
    print("a is vowel")
else:
    print("a is consonant")
    
#.alphabet, digit or special character.

a=input("enter a character")
if a.isalpha():
    print("a is alphabet")
elif a.isdigit():
    print("a is digit")
else:
    print("a is special character")
    
#10.uppercase or lowercase alphabet.
a=input("enter a character")
if a.isupper():
    print("a is uppercase alphabet")
else:
    print("a is lowercase alphabet")    
    
#11. input week number and print week day
a=int(input("enter week number"))
if a==1:
    print("monday")
elif a==2:
    print("tuesday")
elif a==3:
    print("wednesday")
elif a==4:
    print("thursday")
elif a==5:
    print("friday")
elif a==6:
    print("saturday")
elif a==7:
    print("sunday")
else:
    print("invalid week number")
    
    
#input month number and print number of days in that month.
a=int(input("enter month number"))
if a==1 or a==3 or a==5 or a==7 or a==8 or a==10 or a==12:
    print("31 days")
elif a==4 or a==6 or a==9 or a==11:
    print("30 days")
elif a==2:
    print("28 or 29 days")
else:
    print("invalid month number")       
    
    #total number of notes
a=int(input("enter amount"))
hundred= a//100
fifty= (a%100)//50
ten= (a%50)//10
print("number of 100 notes:", hundred)
print("number of 50 notes:", fifty)
print("number of 10 notes:", ten)       

    #triangle and check whether triangle is valid or not
a=int(input("enter side a"))
b=int(input("enter side b"))
c=int(input("enter side c"))
if a+b>c and b+c>a and c+a>b:
    print("triangle is valid")
else:
    print("triangle is not valid")  


#the triangle is equilateral, isosceles or scalene triangle
a=int(input("enter side a"))            
b=int(input("enter side b"))
c=int(input("enter side c"))
if a==b==c:
    print("equilateral triangle")                                           
elif a==b or b==c or c==a:
    print("isosceles triangle")
else:
    print("scalene triangle")
    
    #to find all roots of a quadratic equation.
a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d= b**2 - 4*a*c
if d>0:
    root1= (-b + d**0.5)/(2*a)
    root2= (-b - d**0.5)/(2*a)
    print("real and distinct roots:", root1, root2)
elif d==0:  
    root= -b/(2*a)
    print("real and equal roots:", root)
else:
    real_part= -b/(2*a)
    imag_part= (-d**0.5)/(2*a)
    print("complex roots:", real_part, "+", imag_part, "i and", real_part, "-", imag_part, "i") 
    
#to find profit and loss
cp=int(input("enter cost price"))
sp=int(input("enter selling price"))
if sp>cp:
    profit= sp - cp
    print("profit is:", profit)         
elif cp>sp:
    loss= cp - sp
    print("loss is:", loss)         
else:
    print("no profit no loss")      
    
    #Write a program to print alphabets from a to z
    a=97
while a<=122:
    print(chr(a), end=" ")
    a+=1            
    #2.Write a program to print ASCII values of all characters
a=0
while a<=127:
    print("ASCII value of", chr(a), "is", a)
    a+=1    
    #3.Write a program to print multiplication table of a given number
a=int(input("enter a number"))
for i in range(1, 11):
    print(a, "x", i, "=", a*i)    
#4.Write a program to print first N natural numbers
a=int(input("enter N value"))
for i in range(1, a+1):
    print(i, end=" ")
    
    #Write a program to print all natural numbers in reverse order
a=int(input("enter N value"))
for i in range(a, 0, -1):
    print(i, end=" ")   
    
    #5. to print sum of digits enter by user
a=int(input("enter a number"))
sum=0
while a>0:
    digit= a%10
    sum+= digit
    a//=10
print("sum of digits is:", sum)

#find sum of even numbers between 1 to n
n=int(input("enter n value"))
sum=0
for i in range(1, n+1):
    if i%2==0:
        sum+=i
print("sum of even numbers is:", sum)

#7.sum of odd numbers between 1 to n
n=int(input("enter n value"))
summ=0
for i in range (1, n+1):
    if i%2!=0:
        summ+=i
print("sum of odd numbers is:", summ)   

#swap first and last digit of a number
a=int(input("enter a number"))
str_a= str(a)
if len(str_a)>1:
    swapped_a= str_a[-1] + str_a[1:-1] + str_a[0]
    print("number after swapping first and last digit is:", swapped_a)
else:
    print("number has only one digit, no swapping needed")
    

n=int(input("enter n value"))
sum=0
for i in range(1,n+1):
    sum+=i
print("sum of first n natural numbers is:", sum)    

a=int(input("enter a number"))
str_a=str(a)
if len(str_a)%2==0:
    swapped_a=str_a[len(str_a)//2:] + str_a[:len(str_a)//2]
    print("number after swapping two halves is:", swapped_a)
else:
    print("number has odd number of digits, cannot swap two halves")
    

    