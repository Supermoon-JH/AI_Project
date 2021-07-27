def sum_digit(num):
    result = 0
    for i in str(num):
        result += int(i)
    return result

print("각 자리수의 합: %d" % sum_digit(1234))