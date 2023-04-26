
def commonValues(list1, list2):

    common = []

    for value in list1:

        if value in list2 :

            common.append(value)


    return common
list1 = [-1,0,1, 3, 4, 5,7]
list2 = [-1,-3,4, 5, 6, 7, 9]

commonInteger = commonValues(list1, list2)

print("Common values are : " , commonInteger)



print("-------------QUESTİON 2 ----------------------")


def palindromStrings(strings):

    palindromes = []

    for string in strings:

        if string == string[::-1] :

            palindromes.append(string)

    return palindromes

strings = ["mom", "eye", "software", "chicago", "world","dad"]

palindromes = palindromStrings(strings)

print("Palindrom strings are : ",palindromes)




print("-------------QUESTİON 3----------------------")
def specifyPrimeNumberWithSieve(firstList):
    max_val = max(firstList)
    sieve = [True] * (max_val + 1)
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(max_val ** 0.5) + 1):
        if sieve[i]:
            j = i * i
            while j <= max_val:
                if j in firstList:
                    firstList.remove(j)
                j += i

    return firstList
firstList = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primes = specifyPrimeNumberWithSieve(firstList)
print("Prime numbers are : ",primes)

print("-------------QUESTİON 4----------------------")


def anagrams(word, word_list):
    word_chars = sorted(word.lower().replace(' ', ''))
    anagrams = []

    for string in word_list:
        string = string.lower().replace(' ', '')
        string_chars = sorted(string)
        if string_chars == word_chars:
            anagrams.append(string)

    return anagrams

word = "angle"
word_list = ["leang","ganle","melek","software"]
anagramList = anagrams(word,word_list)
print("Anagram words are : " , anagramList)