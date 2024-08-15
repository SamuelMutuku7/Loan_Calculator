string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
vowel_count = []

for item in string:
    if item in vowels:
        vowel_count.append(item)

print(len(vowel_count))