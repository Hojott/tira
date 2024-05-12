def count(t):
    all_seqs = {} # last num : seqs

    for v in t:
        if v not in all_seqs:
            all_seqs[v] = 1
        else:
            all_seqs[v] += 1

        for last in all_seqs:
            if v > last:
                all_seqs[v] += all_seqs[last]

    return sum(all_seqs.values())

if __name__ == "__main__":
    print(find([1, 1, 2, 2, 3, 3])) # [1, 2, 3]
    print(find([1, 1, 1, 1])) # [1]
    print(find([5, 4, 3, 2, 1])) # [3]
    print(find([4, 1, 5, 6, 3, 4, 1, 8])) # [1, 3, 4, 8]
    print(find([46, 75, 87, 33, 75, 65, 42, 64, 82, 3, 98, 38, 20, 88, 21, 68, 59, 12, 73, 63, 49, 71, 17, 28, 97, 25, 22, 16, 83, 60, 61, 28, 82, 48, 92, 44, 87, 83, 71, 91, 54, 43, 66, 49, 49, 12, 87, 99, 69, 6, 42, 48, 32, 39, 50, 87, 84, 83, 89, 77, 47, 10, 72, 41, 100, 20, 32, 88, 40, 23, 36, 34, 73, 6, 20, 58, 31, 6, 84, 53, 29, 56, 48, 33, 98]))
    print(find([52, 86, 10, 61, 13, 43, 33, 34, 87, 38, 13, 15, 11, 52, 75, 4, 79, 66, 12, 30, 85, 26, 88, 36, 90, 83, 72, 38, 60, 26, 81, 34, 39, 74, 57, 80, 72, 98, 41, 73, 100, 33, 21, 44, 45, 75, 73, 25, 88, 46, 58, 84, 25, 69, 13, 94, 2, 92, 60, 46, 70, 13, 51, 72, 81, 89, 87, 18, 45, 33, 60, 53, 57, 16, 72, 5, 34, 71, 92, 39, 22, 79, 31, 3, 20, 79, 26, 2, 18, 74, 14, 63, 91, 3, 45, 19]))
