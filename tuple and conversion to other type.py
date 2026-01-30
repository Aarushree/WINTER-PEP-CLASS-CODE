# colors=("red","green","blue")
# print(colors[1])
# print(colors[2])

'''==============================================conversion=========================================================================='''

#we have to convert list into a tuple
# numbers=[1,2,3,4]
# print(type(numbers))
# numbers_tuple=tuple(numbers)
# print(type(numbers_tuple))
# print(numbers_tuple)

#conversion of tuple to list
# colors=("red","green","blue")
# print(type(colors))
# colors_list=list(colors)
# print(type(colors_list))
# print(colors_list)

#conversion of ist to set
# nums=[1,2,2,3,4,4]
# nums_set=set(nums)
# print(nums_set)
# nums_list=list(nums_set)
# print(nums_list)

#conversion of dictonary into a set
# student ={"name":"karan","age":24}
# student_set = set(student)
# print(type(student_set))
# print(student_set)

#conversion of set into a dictionary
subjects = {"maths","science","english"}
sub_dict=dict.fromkeys(subjects,0)
print(sub_dict)
