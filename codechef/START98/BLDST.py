for i in range(int(input())):
    n, m = map(int, input().split())
    balls = list(map(int, input().split()))
    ballsum = sum(balls)
    ans = 0
    if ballsum<=n*(m-1):
        print(ans)
        continue
    elif ballsum==n*m:
        print(ballsum)
    else:
        print(ballsum%n)