# #to create a list
# number=[10,20,30,40]
# #looping through the list
# for i in number:
#     print(i)
# fruit=[]
# print(fruit)
# #append is used to dd element in last
# fruit.append("apple")
# print(fruit)

#find the sum of all element in a list
# number=[5,10,15]
# total=0
# for i in number:
#     total=total+i
# print(total)



# Q Reverse a list
# nums=[1,2,3,4]
# reversed_list = nums[::-1]
# print(reversed_list)

# Q Remove duplicate element from the list
nums=[1,2,2,3,4,4]
unique = []
for i in nums:
    if i  not in unique:
        unique.append(i)
print(unique)

