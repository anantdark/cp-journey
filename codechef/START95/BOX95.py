INT_MAX = 10**18
print(INT_MAX)
for i in range(int(input())):
    len = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    boxes = [[INT_MAX]] 
    xor = [INT_MAX]
    while arr:
        val = arr.pop(-1)
        for box in boxes:
            # if 
            pass