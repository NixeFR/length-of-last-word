def lengthOfLastWord(s):
    x = s.rstrip(' ')
    list(x)
    lastIndex = len(x) - x[::-1].index(' ') - 1
    myres = 0
    for i in range(lastIndex, len(x)-1):
        myres += 1
    return myres

print(lengthOfLastWord("   fly me   to   the moon  "))
