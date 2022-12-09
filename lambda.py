# list1=[3,4,10,9,18,66,13,15]
#  evenNum=list(filter(lambda i:i%2==0,list1))
#  print(evenNum)

# squareNum=list(map(lambda i: i**2,list1))   
# print(squareNum)


# list1=[10,20,30,40,50]
# #triple the values of list
# triple=list(map(lambda i:i*3,list1))
# print(triple)

# list2=["a","B","C","D","e","f"]
# num=list(map(lambda i:i==1,list2.swap))
# print(num)
# def div(a,b):
#     print(a/b)
# def good_div(func):
#     def inner_div(a,b):
#         if a<b:
#             a,b=b,a
#         return func(a,b)
#     return inner_div
# div=good_div(div)
# div(2,4)         

from functools import reduce
list1=[1,2,3,4,5,6]
sum=reduce(lambda i,j:i+j,list1)
print(sum)