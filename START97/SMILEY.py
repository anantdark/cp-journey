for i in range(int(input())):
    length = int(input())
    smiley = input()
    smiley.strip("()")
    reduced = ''
    for alpha in smiley:
        if not reduced or reduced[-1]!=alpha:
            reduced += alpha
    smiles = 0
    for i in range(len(reduced)):
        if i+3>len(reduced):
            break
        else:
            if reduced[i:i+3] == ":):":
                smiles+=1
    print(smiles)