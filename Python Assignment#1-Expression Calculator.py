x = input("Please Enter a Mathmetical Expression e.g. 2+4/3*44/5-4")
plus = 0   
minus = 0
divide = 0
multiply = 0
count = 0
status = False
Exp = []
for val in x:
    count += 1
    if(count == 1):
        Exp.append(val)
        
    else:
        if(val != "+" and val != "-" and val != "*" and val != "/"):            
            if(Exp[count-2] != "+" and Exp[count-2] != "-" and Exp[count-2] != "*" and Exp[count-2] != "/"):
                Exp[count-2] += val
                count -= 1
                
            else:
                Exp.append(val)
        else:
             Exp.append(val)          
             

    
    if(val == "+"):
        plus += 1
    elif(val == "-"):
        minus += 1
    elif(val == "*"):
        multiply += 1
    elif(val == "/"):
        divide += 1


while divide >= 1:
    index = Exp.index("/")
    if(int(Exp[index+1]) == 0):
        status = True
        print("Please insert a valid expression: Division by Zero Error Found")
        break
    else:        
        Exp[index-1] = int(Exp[index-1]) / int(Exp[index+1])
        del Exp[index]
        del Exp[index]
        divide -= 1  

while multiply >= 1:
    index = Exp.index("*")
    Exp[index-1] = int(Exp[index-1]) * int(Exp[index+1])
    del Exp[index]
    del Exp[index]
    multiply -= 1 
    
while plus >= 1:
    index = Exp.index("+")
    Exp[index-1] = int(Exp[index-1]) + int(Exp[index+1])
    del Exp[index]
    del Exp[index]
    plus -= 1 
    
while minus >= 1:
    index = Exp.index("-")
    Exp[index-1] = int(Exp[index-1]) - int(Exp[index+1])
    del Exp[index]
    del Exp[index]
    minus -= 1 

    
if(status != True):    
    result = Exp[0]
    print("The Result of desired expression is = "+ str(result))
