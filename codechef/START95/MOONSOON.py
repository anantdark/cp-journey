for i in range(int(input())):
    effective_energy = 0
    cars, chargers, hours = map(int, input().split())
    capacity = list(map(int, input().split()))
    power = list(map(int, input().split()))
    if cars>chargers:
        capacity = sorted(capacity)[-chargers:]
        power.sort()
    elif cars<chargers:
        power = sorted(power)[-cars:]
        capacity.sort()
    else:
        power.sort()
        capacity.sort()
    for i in range(min(chargers, cars)):
        total_energy = (power[i]*hours)
        effective_energy += total_energy if total_energy<=capacity[i] else capacity[i]
    print(effective_energy)