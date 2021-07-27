def gcd(x, y):
    while True:
        if x == y :
            return x
        elif x > y :
            x = x - y
        else :
            y = y - x

num1 = 30
num2 = 18

print("최대공약수 = ", gcd(num1, num2))