# Problem 1:

# Find the password strength.
# For each substring of the password which contains at least one vowel and one consonant, its strength goes up by 1.
# vowels={'a', 'e', 'i', 'o', 'u'}, and rest of letters are all consonant.
# (Only lower alphabet letters)
# Input:
# thisisbeautiful
# output:
# 6
# explaination:
# this, is, be, aut, if, ul

# input:
# hackerrank
# output:
# 3
# explaination:
# hack, er, rank


def password(word):
    vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    vowel = 0
    consonent = 0
    count = 0
    for i in word:
        if vowels.get(i, None) is not None:
            vowel += 1
        else:
            consonent += 1
        if vowel >= 1 and consonent >= 1:
            count += 1
            vowel = 0
            consonent = 0
    return count
