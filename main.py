s = int(input())
n1 = " программистов"
n2 = " программист"
n3 = " программиста"
if s >= 0:
    if s == 0:
        print(str(s) + n1)
    elif 10 <= s % 100 <= 20:
        print(str(s) + n1)
    elif s % 10 == 1:
        print(str(s) + n2)
    elif 2 <= s % 10 <= 4:
        print(str(s) + n3)
    else:
        print(str(s) + n1)
