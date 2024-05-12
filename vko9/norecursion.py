def count_sequences(n, result={}):
    """ from tehtävänanto """
    if n == 0:
        return 1
    if n not in result:
        count = 0
        for i in range(2, n + 1, 2):
            count += count_sequences(i - 2) * \
                     count_sequences(n - i)
        result[n] = count
    return result[n]

def count_sequences_recursiont(n):
    result = {}
    result[0] = 1
    for i in range(2, n+1, 2):
        result[i] = 0
        for j in range(2, i + 1, 2):
            result[i] += result[j - 2] * result[i - j]

    return result[n]

if __name__ == "__main__":
    print(count_sequences(100))
    print(count_sequences_recursiont(100))
