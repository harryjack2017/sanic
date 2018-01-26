'''
    摘要算法

'''

import hashlib

'''md5'''
str1 = "how to user hashlib"
str2 = " in your work?"
md5 = hashlib.md5()

md5.update((str1 + str2).encode("utf-8"))
print(md5.hexdigest())

### 一句话分开加密
md5 = hashlib.md5()
md5.update(str1.encode("utf-8"))
md5.update(str2.encode("utf-8"))
print(md5.hexdigest())

###sha1加密

sha1 = hashlib.sha1()
sha1.update(str1.encode("utf-8"))
sha1.update(str2.encode("utf-8"))
print(sha1.hexdigest())

sha2 = hashlib.sha1()
sha2.update((str1 + str2).encode("utf-8"))
print(sha2.hexdigest())

###hmac 将key混入计算中

import hmac

str1 = b"how to user hashlib"
str2 = b" in your work?"
h = hmac.new(str1, str2, digestmod="MD5")
print(h.hexdigest())
