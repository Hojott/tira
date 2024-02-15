import time

def find(N):
    str1 = "a"
    str2 = "a"
    while 1:
        str2 += "a"
        if hash(str1) % N == hash(str2) % N:
            return (str1, str2)

if __name__ == "__main__":
    start = time.time()
    print(find(1000000)) # esim. ('abc', 'aybabtu')
    print(time.time() - start)
