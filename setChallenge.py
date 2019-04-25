myString = "This is a String"

vowels_tuple = ('a', 'e', 'i', 'o', 'u')

vowels = set(vowels_tuple)

notVowels = []

for i in myString:
    if i == ' ':
        continue
    if i in vowels:
        continue
    else:
        notVowels.append(i)

print(sorted(notVowels))

with open('timesTables.txt', 'a') as timesTable:

    for i in range(1, 13):
        x = 2 * i
        print("{0} times 2 is {1}".format(i, x), file=timesTable)

