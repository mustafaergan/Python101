#LOOPS

# while
print("** while")

count = 0

while (count < 10):
        print("*****")
        count = count +1
        print(count, " Count")
        
print("** while-else")        
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")

#while (count > 5): count = count + 1 

#RANGE
print("**range")
reng = range(4, 10)
print(reng)

#FOR
print("**for")
for num in range(1,5): 
    print(num)
    
print("**nested for")    
for i in range(1,3):
    for j in range(i+3):print("*")
    
    
print("**String for")   
text ="Hello"
for i in text:
    print(i)
    
print("**multiplication table")     
for i in range(1,11):
    for j in range(1,11):
        k=i*j
        print (k, end=' ')
    print()


