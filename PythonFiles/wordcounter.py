# Take the users input.
with open('paperinput.txt') as f:
    text = f.readlines()

# Add all the lines together.
string = ''
for line in text:
    string += line + " "

# Normalize
words = string.lower().replace(".", "").replace(",", "").replace("(", "").replace(")", "").split()
d = {}

# Identify the number of words.
while len(words) > 0:
    word = words[0]
    occurences = words.count(word)
    d[word] = occurences
    for i in range(occurences):
        words.remove(word)

# Sort by number of uses.
d = sorted(d.items(), key=lambda x: x[1], reverse=True)

# Output the results. The easy part.
print('\n\nYou used:')
for item, val in d:
    print(f'{item} : {val} times!')
    
