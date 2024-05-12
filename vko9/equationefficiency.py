from math import factorial, floor

def count_sequences(n):
    m = n//2

    return floor(factorial(n) / ((m + 1) * (factorial(m)**2)))

if __name__ == "__main__":
    print(count_sequences(100))
