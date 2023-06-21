from collections import Counter
arr = list()
final_str = []  
for i in range(int(input())):
    arr.append(input())
counter = Counter(arr)
for i in arr:
    if counter[i]>1:
        counter[i]-=1
    else:
        final_str.append(i[-2::])
final_str.reverse()
print(''.join(final_str))