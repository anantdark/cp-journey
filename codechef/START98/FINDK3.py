# cook your dish here
for i in range(int(input())):
    a, b, c = map(int, input().split())
    if (b*c)%a==0:
        print(b*c, a)
    elif (a*c)%b==0:
        print(a*c, b)
    elif (a*b)%c==0:
        print(a*b, c)
    else:
        print(-1)