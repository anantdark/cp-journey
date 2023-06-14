MOD = 10**9 + 7
vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(int(input())):
    length, k = map(int, input().split())
    word = input()
    vowel_counter = 0
    word_split = list()
    temp_list = list()
    perm = 0
    final = []
    for i in range(len(word)):
        if word[i] in vowels:
            vowel_counter+=1
        temp_list.append(word[i])
        if vowel_counter==k:
            word_split.append(temp_list)
            vowel_counter = 0
            temp_list = list()
    
    for j in range(1, len(word_split)):
        current_word = word_split[j]
        for k in range(len(current_word)):
            if current_word[k] not in vowels:
                perm+=1
            elif current_word[k] in vowels:
                final.append(perm+1)
                perm = 0
                break
    final_temp=1
    for i in final:
        final_temp = (final_temp*i)%MOD
    print(final_temp)


# mangoman
# ma ngo man ma ngom an
# man go man man gom an
# mang o man mang om an

