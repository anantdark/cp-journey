for i in range(int(input())):
    length = int(input())
    arrival = list(map(int, input().split()))
    departure = list(map(int, input().split()))
    count = dict()
    arrival.extend(departure)
    max = 0
    for runway in arrival:
        if runway in count.keys():
            count[runway]+=1
        else:
            count[runway] = 1
        if count[runway] > max:
            max = count[runway]
    print(max)