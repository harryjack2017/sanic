# try:
#     f = open("./test1.txt", "r")
#     print(f.read())
#
# except Exception as e:
#     print("Error", e)
#
# finally:
#     if f:
#         f.close()
#     print("closed")

# with open("./test.txt","r") as f:
#     print(f.read())

# f=open("./test.txt","r")
# for line in f.readlines():
#     print(line.strip())

### 读取图片,以二进制形式

f=open("./python.jpeg", "rb")
print(f.read())



### 写文件，然后读
f=open("./test.txt","w")
f.write("hello world")
f.close()
f=open("./test.txt","r")
print(f.read())
f.close()

### with 更保险
with open("./test.txt","w") as f:
    f.write("good mornign")



with open("./test.txt","a") as f:
    f.write(",good afternoon")