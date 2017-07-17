#List
list1 = ['mustafa', 'ergan', 1987, 22, 30];

print("list1")
print(list1)

print("list1[1],list1[2]")
print(list1[1],list1[2])

list1[1] = 2017

print("list1")
print(list1)


print("list1[2:5]")
print(list1[2:5])

print("list1[1:]")
print(list1[1:])

del list1[2]

print("list1")
print(list1)

print("list1[-2]")
print(list1[-2])

print("len")
print(len(list1))

print("len and range")
list2 = list(range(5))
print(list2)
print(len(list2))

print("max")
print(max(list2))

print("max String")
list3 = ['mustafa', "zebra", 'ergan', "ankara"];
print(max(list3))

print("min")
print(min(list2))

print("min String")
list3 = ['mustafa', "zebra", 'ergan', "ankara"];
print(min(list3))


#seq 
list4 = list( "Java - Python" )

print ("List elements : ", list4)
