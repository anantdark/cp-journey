for i in range(int(input())):
    rolls = list(map(int, input().split()))
    alice = rolls[:3]
    bob = rolls[3:]
    alice.remove(min(alice))
    bob.remove(min(bob))
    alice = sum(alice)
    bob = sum(bob)
    if alice>bob:
        print("Alice")
    elif bob>alice:
        print('Bob')
    else:
        print('Tie')