for i in range(int(input())):
    train_max = 0
    counter = {'A': 0, 'B': 0, 'AB': 0, 'O': 0}
    length = int(input())
    arr = list(input().split(' '))
    for blood in arr:
        counter[blood] += 1
    if counter['AB']:
        train_max = counter['AB']
    if counter['A'] or counter['B']:
        train_max += max(counter['A'], counter['B'])
    train_max += counter['O']
    print(train_max)
