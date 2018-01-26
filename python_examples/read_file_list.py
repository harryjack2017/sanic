if __name__ == "__main__":
    import string

    fp = open("./test1.txt")
    a = fp.read()
    fp.close()

    fp = open("./test2.txt")
    b = fp.read()
    fp.close()

    l = list(a + b)
    l.sort()
    s = ''.join(l)

    fp = open("./test3.txt", "w")
    fp.write(s)
    fp.close()
