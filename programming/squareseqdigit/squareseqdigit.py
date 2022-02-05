def squareSequenceDigit(n):
    result = []
    for i in range(1, n+1):
        number_lst = []
        number = i * i
        while number > 0:
            number_lst.append(number%10)
            number //= 10
        number_lst.reverse()
        result.extend(number_lst)
    print(result[n-1])
    return result[n-1]
