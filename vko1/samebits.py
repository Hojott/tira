def count(s):
    ones = 0
    for bit in s:
        if bit == "1":
            ones += 1
    
    zeros = len(s) - ones

    return ones if ones < zeros else zeros

if __name__ == "__main__":
    print(count("01101")) # 2
    print(count("1111")) # 0
    print(count("101111")) # 1
    print(count("00001111")) # 4
