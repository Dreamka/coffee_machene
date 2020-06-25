string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'
count = 0

# fix this for loop
for letter in string.strip(vowels):
    if letter in vowels:
        count += 1