from datetime import datetime

#Object # 1
    
def circle_area(radius,phi=22/7):
     area = phi * (radius*radius)
     print("Area of Circle is = {}".format(round(area,2)))


#Object # 2

def check_num(num):
    try:
        num = float(num)
        if num > 0:
            print("The Number "+str(num)+ " is Positive")
        elif num < 0:
            print("The Number "+str(num)+ " is Negative")
        elif num == 0:
            print("The Number "+str(num)+ " is Zero")
        
    except:
        print("Invalid Input please insert a valid number")
        check_num(input("Please Enter a Number to check is either positive, Negative or Zero \n"))
    

#Object # 3

def check_divisibility(numerator,denominator):    
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        if numerator%denominator == 0:
            print("The number " + str(numerator)+ " is completely Divisible by " + str(denominator))
        else:
            print("The  " + str(numerator)+ " is not completely Divisible by " + str(denominator))
    except:
        print("Please Enter a Correct number ")
        check_divisibility(input("Please Enter a Numerator \n"),input("Please Enter a Denominator \n"))
        
  
#Object # 4

def calc_days(first_date,second_date):
    print("Number of days between "+ str(first_date) + " and " + str(second_date) + " is: " +  str((second_date-first_date).days)+ " Days")    

#Object # 5

def sphere_volume(radius,phi=22/7):
    volume = (4/3) * phi * (radius*radius*radius)
    print("The Volume of Sphere is = {}".format(round(volume)))

#Object # 6

def copy_str(string,frequency):
    print(str(frequency)+ " Copies of String " + string + " is: " + (string*frequency))

    

#Object # 7

def check_even_odd(num):
    try:
        num = int(num)        
        if num % 2 == 0:
            print("The number " + str(num)+ " is Even")
        elif num % 2 == 1:
            print("The number " + str(num)+ " Odd")
    except:
        print("Please Enter a Correct number ")
        check_even_odd(input("Please Enter a Number to check even or odd \n"))  
        

#Object # 8
    
vowels = ["A","E","I","O","U"]
def check_vowel(vowel,character):
    if character.upper() in vowel:
        print("Character "+ character + " is Vowel" )
    else:
        print("Character "+ character + " is Not Vowel" )

    
#Object # 9

def triangle_area(base,height):
    area = (base*height)/2
    print("The Area of Triangle is = {}".format(round(area)))


#Object # 10
        
def calc_interest(principal_amount,roi,num_of_years):
    try:
        principal_amount = float(principal_amount)
        roi = float(roi)
        num_of_years = float(num_of_years)
        
        #amount = (((principal_amount*roi)/100)* num_of_years) + principal_amount
        amount = round(principal_amount*((1+roi)**(5)),2)
        print("After "+ str(num_of_years) + " Years"+ "Your Principal Amount "+ str(principal_amount) + " over an interest rate of " + str(roi) + " is: " + str(amount))
    
    except:
        print("Please Enter a Valid values ")
        calc_interest(input("Please Enter a Pricipal Amount: \n"),input("Please Enter a rate of interest in %: \n"),input("Please Enter number of years of investment: \n"))
        


#Object # 11

def euclidean_distance(x1,x2,y1,y2):
    print("Euclidean Distance is {}".format((((x1-y1)**2) + ((x2-y2)**2))**(1/2)))

    
#Object # 12    

def feet_to_cm(height):
    print("There are {} cm in {} ft. of height".format(round((height*30.48),2),height))


#Object # 13

def calc_bmi(height,weight):
    print("Your BMI is {} ".format(round(weight/((height*0.01)**2),2)))


#Object # 14

def sum_integers(num):
    print("Sum of n positive integers till {} is {}".format(num,(num * (num + 1)) / 2))
    
   
#Object # 15

def sum_digits(num):
    sum = 0
    for e in num:
        sum += int(e)
    print("The sum of all digits of {} is {} ".format(num,sum))

#Object # 16

def dectobin(num):
    
    if num > 1:        
        dectobin(num // 2)        
    print(num % 2,end = "")
    
#Object # 17
 
def bintodec(num): 
    decimal = i = n = 0
    bin_num = num
    while(num != 0): 
        dec = num % 10
        decimal = decimal + dec * pow(2, i) 
        num = num//10
        i += 1
    print("The Representation of {} is {}".format(bin_num,decimal))

    

#Object # 18

def count_vowel_consonant(string):    
    vowels = ["A","E","I","O","U"]
    vowel = 0
    consonant = 0
    for e in string:
        if e.upper() in vowels:
            vowel += 1
        else:
            consonant += 1
    print("Vowels = {}".format(vowel))
    print("Consonants = {}".format(consonant))

    
#Object # 19

def palindrome(string):
    if string[::-1] == string:
        print("The String {} is Palindrome".format(string))
    else:
        print("The String {} is Not Palindrome".format(string))
        

        
#Object # 20

def count_sans(string):
    alphabets = digits = special = 0
    spaces = string.count(' ')
    for e in range(len(string)):
        if string[e].isalpha():
            alphabets += 1
        elif string[e].isdigit():
            digits += 1
        else:
            special += 1
    print("Numbers = {}".format(digits))
    print("Alphabets = {}".format(alphabets))
    print("Special = {}".format(special-spaces))
    print("Spaces = {}".format(spaces))


#Object # 21

def pattern1():
    for i in range(0,5):
        for j in range(0,i+1):
            print("*",end =' ')
        print("\r")

    for e in range(5,0,-1):
        for f in range(0,e-1):
            print("*",end = ' ')
        print("\r")


        
#Object # 22

def pattern2():
    for i in range(1,6):
        for j in range(1,i+1):
            print(j,end =' ')
        print("\r")

    for e in range(6,1,-1):
        for f in range(1,e-1):
            print(f,end = ' ')
        print("\r")
        
#Object # 23

def pattern3():
    for i in range(1,10):
        for j in range(1,i+1):
            print(i,end =' ')
        print("\r")
