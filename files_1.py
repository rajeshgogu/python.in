# f = open("demo1.txt","r")
# # print(f.read())
# print(f.readline())
# print(f.readline())
# f1  = open("demo1.txt","w")
# f2 = open("introduction.txt","w")
# f2.writelines("This is Rajesh")


# f = open("img_copy.png","rb")
# f1 = open("img_copy_copy.png","wb")
# print(f.read())
# for i in f:
#     f1.write(i)

# import os
# os.remove("demo1.txt")
#try:
    #this block of code will run and throw errors if there are any
#except:
# this will raise the errors
# else:
# this will execute if there are no errors
# finally:
# this will execute regardless the result of try and except


# try:
#     f = open("demo.py")
#     try:
#         f.write("ABC")
#     except:
#         print("Error in file")
#     finally:
#         f.close()
# except:  


a = 5
if a < 10:
    raise Exception("Value is less than 5")