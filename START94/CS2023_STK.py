for i in range(int(input())):
    days = int(input())
    om = list(map(int, input().split()))
    addy = list(map(int, input().split()))
    om_max, addy_max, counter = 0, 0, 0
    for i in om:
        if i != 0:
            counter += 1
        else:
            om_max = max(counter, om_max)
            counter=0
    om_max = max(counter, om_max)
    counter=0
    for i in addy:
        if i != 0:
            counter += 1
        else:
            addy_max = max(counter, addy_max)
            counter = 0
    addy_max = max(counter, addy_max)
    if om_max<addy_max:
        print('Addy')
    elif om_max>addy_max:
        print('Om')
    else:
        print('Draw')
