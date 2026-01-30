'''Ques1. Move all zeros to the end '''
# nums=[0,1,0,3,12]

# result=[]# we will store non zero elements
# zero_count=0
# for n in nums:
#     if n==0:
#         zero_count+= 1
#     else:
#         result.append(n)

# for i in range(zero_count):
#     result.append(0)
# print(result)

#checking palindorme  with two pointer
# text="naman"
# left=0
# right=len(text)-1
# is_Palindrome=True
# while left<right:
#     if text[left]!=text[right]:
#         is_Palindrome = False
#         break
#     left +=1
#     right -=1
# print(is_Palindrome)

'''Ques: find the longest in a sentences'''
# sentence="Python makes problem solving fun"
# words=sentence.split()
# longest=""
# for i in words:
#     if len(i)>len(longest):
#         longest=i
# print(longest)


'''Question: A=[1,2,3,2] target=3 count =2'''
# nums = [1,2,3,2]
# target = 5
# count = 0
# for i in range(len(nums)):
#     total = 0
#     for j in range(i,len(nums)):
#         total += nums[j]
#         if total == target:
#             count+=1
# print(count)

nums=[2,7,11,15]
target = 9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        #check if sum matches the target
        if nums[i]+nums[j]==target:
            print(nums[i],nums[j])


nums=[2,7,11,15]
target = 9
left =0
right = len(nums)-1
while left<right:
    current_sum = nums[left]+nums[right]
    if current_sum==target:
        print(nums[left],nums[right])
        break
    elif current_sum<target:
        left+=1
    else:
        right-=1