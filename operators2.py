#comparison opperators
#these compare two values and return a boolon
#in mathwmatic we have opperator like.< ,>

#lets declare some variable
num1 = 20
num2 = 40
print(num1 < num2) #less than
print(num1 > num2) #greator than
print(num1 >= num2) #greator than or equal to
print(num1 <= num2) #less than or equal to
print(num1 != num2) #not equal to
print(num1 == num2) #not equals to

#write comment on top of the line you want to comment about

#logical opperators
#we have the following and (&), or(||), not(!)
log1 = 5
log2 =6
print((log1  > log2) and (log2 < log1)) #true when everything is different
print((log1 > log2) or (log2 < log1)) #true when everything are the same
print(True and True)
print(True and False)
print(not True)
print(True or True)
print(False or False)
print(True or False)
print(False or True)

#membership opperators
numbers = (20,30,40,50)
print(20 in numbers)
print(20 not in numbers)

name = "ozzy"
print("o" not in name)
print("O" not in name)

#identity opperators
#we have is,not is
print(20 is not numbers)
print(20 is 20)




