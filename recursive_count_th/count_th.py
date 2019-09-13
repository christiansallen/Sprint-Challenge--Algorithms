'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

'''
Check is word is less than 2 characters, if it is return 0
delcare global index and count to increment
base case is when index equals length of word - 1
If word[index] is t and word[index+1] = h then increment count by 1
use recursion to call this as many times before base case if reached
'''

index = 0
count = 0


def count_th(word):

    global index
    global count

    if(len(word) < 2):
        return 0

    if(index == len(word)-1):
        return count

    if word[index] == 't' and word[index+1] == 'h':
        count += 1

    index += 1

    return count_th(word)


print(count_th('therthhe thereth'))
