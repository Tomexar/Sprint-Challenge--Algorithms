'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    TH = len('th')
    L = len(word)
    lower = word
    #lower = word.lower()
    print (lower)

    if L == 0 or L < 2:
        return 0
    elif lower[0:2] == 'th':
        return count_th(lower[1::]) +1
    else:
        return count_th(lower[1::])
   
    # count = 0

    # for i in range(L - TH + 1):
    #     j = 0

    #     for j in range(TH):
    #         if (lower[i + j] != 'th'):
    #             break
    #     if (j == TH -1):
    #         count += 1
    #         j = 0 
    # print(lower.count('th'))

print(count_th('THtHThth'))