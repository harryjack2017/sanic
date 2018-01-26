

class Student(object):

    def __init__(self, name):
        self.name =  name
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")

        if value < 0 or value > 100:
            raise ValueError("score must between 0 and 100")

        self._score = value


    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value, int):
            raise ValueError("score must be an integer")

        if value<0 or value >100:
            raise ValueError("score must between 0 and 100")

        self._score = value

    # 直接对实例进行调用

    def __call__(self):
        print("my name is %s." % self.name)



s=Student("jim")

s.set_score(100)

#print(s.get_score())

s.score=60

#print(s.score)


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a , self.b = self.b, self.a+ self.b

        if self.a>100:
            raise StopIteration()

        return self.a

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a



for n in Fib():
    print(n)


f= Fib()
print(f[10])



class Chain(object):
    def __init__(self, path = ""):
        self._path= path

    def __getattr__(self, path):
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path

    __repr__=__str__



print(Chain().status.user.time.list)

s = Student("mis")

print(s())