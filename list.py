list1=[]
list2=[1,2,3,4]
list1.extend(list2)
# list1=list2.copy()
list2.clear()
for item in list1:
    list2.insert(0,item)
print(list2)
# OR
# print(list1[::-1])

a='Abracadabra'
del a
# print(a) // a is deleted so it doesn't work