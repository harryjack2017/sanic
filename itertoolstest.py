import itertools

natuals = itertools.count(1)

# for n in natuals:
#     if n < 100:
#         print(n)

###将一个元素无限重复下去，第二个参数限定重复次数
ns = itertools.repeat("A", 3)
for n in ns:
    print(n)

###taskwhile    根据条件判断，截取有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x < 10, natuals)
print(list(ns))

### chain 将一组迭代对象串联起来，形成一个更大的迭代器

for c in itertools.chain("ABC", "XYZ"):
    print(c)

### groupby：把迭代器中相邻的重复元素跳出来，放在一起
for key, group in itertools.groupby("AAABBBCCCAA"):
    print(key, list(group))

###如果忽略大小写，进行分组，则添加匿名函数
for key, group in itertools.groupby("AaaBbCc", lambda c: c.upper()):
    print(key, list(group))

##@contextmanager:

from contextlib import contextmanager


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print("query info about %s..." % self.name)


@contextmanager
def create_query(name):
    print("begin")
    q = Query(name)
    yield q
    print("End")


with create_query("boc") as q:
    q.query()


@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("<%s>" % name)


with tag("h1"):
    print("hello")
    print("world")

# from contextlib import closing
# from urllib.request import urlopen
#
# with closing(urlopen('https://www.python.org')) as page:
#     for line in page:
#         print(line)