a = int(input("1. Enter a number: "))
b = int(input("2. Enter a number: "))
c = int(input("3. Enter a number: "))

avg = (a + b + c) / 3
print("Average = ", avg)

if avg > a and avg > b and avg > c:
    print("% is greater than a, b, c"%(avg, a, b, c))