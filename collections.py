
###namedtuple:创建自定义的tuple
from collections import namedtuple

Point = namedtuple("Point", ["x", "y", "z"])

p = Point(1, 2,3)

print(p.x)

print(isinstance(p, Point))
print(isinstance(p,tuple))

circle=namedtuple("circle",["x","y","r"])

c=circle(1,2,3)
print(c.r)


## deque：高效实现插入删除的双向列表，适合于队列和栈
from collections import deque

l=['a','b','c']
l.append('d')
l.remove("d")
l.pop()
print(l)

q=deque(l)
q.append('x')
q.appendleft('y')
q.popleft()
print(q)


##defaultdict:为引用的key添加默认值
from collections import defaultdict
dd=defaultdict(lambda:"N/A")
dd["key1"]="abcd"
print(dd["key1"])
print(dd["key2"])


##OrderedDict   保持key的排序


##Counter 统计字符出现的次数
from collections import Counter
c=Counter()
for ch in "programming":
    c[ch]= c[ch]+1
print(c)
