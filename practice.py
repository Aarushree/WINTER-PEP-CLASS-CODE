# print(True+True+True)
# print("5"+"4")
# print("5"*10)
# def change(x):
#     x+=10
# a=5
# change(a)
# print(a)

# def update(list):
#     list.append(10)
# nums = [1,2,3]
# update(nums)
# print(nums)


# t=(1,2,3)
# t=t+(4,)
# print(t)

# s={1,2,2,3,3}
# print(len(s))

# i=1
# while i<10:
#     i*=3
#     print(i)

# for i in range(3):
#     print(i)
# else:
#     print("done")

# try:
#     print("A")
#     10/0
#     print("B")
# except:
#     print("C")
# print("p")

# try:
#     print(1)
# except:
#     print(2)
# finally:
#     print(3)

def test():
    try:
        return 10
    finally:
        return 20
print(test())