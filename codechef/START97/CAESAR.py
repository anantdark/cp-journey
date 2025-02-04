def alphaconvertor(val):
    return val+97
def originconvertor(val):
    return (ord(val)-97)

def ciphergen(ques, discord):
    finstr = ''
    for alphabet in ques:
        val = originconvertor(alphabet)
        val = (val+discord)%26
        val = alphaconvertor(val)
        finstr += chr(val)
    return finstr

for i in range(int(input())):
    length = int(input())
    sample = input()
    sample_ans = input()
    ques = input()
    sample_inp = originconvertor(sample[0])
    sample_out = originconvertor(sample_ans[0])
    discord = sample_out - sample_inp
    if discord<0:
        discord = discord + 26
    print(ciphergen(ques, discord))
