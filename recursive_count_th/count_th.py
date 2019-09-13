'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

index = 0
count = 0


def count_th(word):

    global index
    global count

    if(index == len(word)-1):
        return count

    if word[index] == 't' and word[index+1] == 'h':
        count += 1

    index += 1

    return count_th(word)


print(count_th('therthhe thereth'))
