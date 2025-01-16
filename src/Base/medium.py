def getVowelList(string):
    vowel = "AEIOU"
    return sum([len(string[i:]) for i in range(len(string)) if string[i] in vowel])

def getWinner(cVowels, cConstants):
  
    if cConstants == cVowels:
        return "Draw"

    if cConstants > cVowels:
        winner = "Stuart " + str(cConstants)
    else: 
        winner = "Kevin " + str(cVowels)
    return winner
    
def minion_game(string):
    length = len(string)
    if length <= 0 or length >= pow(10,6):
        return 0
    posibleCombination = ((length) * (length + 1))/2

    vowlCount = getVowelList(string)
    
    consonatsCount = posibleCombination - vowlCount
    
    return getWinner(vowlCount, consonatsCount)
