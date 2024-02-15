def find(s):
    for i in range(len(s)):
        subs = s[0:i+1]
        if subs * (len(s)//len(subs)) == s:
            return len(subs)

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7
