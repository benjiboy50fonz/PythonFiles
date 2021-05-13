prepositions = [
    'about.',
    'below.',
    'excepting.',
    'off.',
    'toward.',
    'above.',
    'beneath.',
    'for.',
    'on.',
    'under.',
    'across.',
    'besides.',
    'beside.',
    'from.',
    'onto.',
    'underneath.',
    'after.',
    'between.',
    'in.',
    'out.',
    'until.',
    'against.',
    'beyond.',
    'outside.',
    'up.',
    'along.',
    'but.',
    'inside.',
    'over.',
    'upon.',
    'among.',
    'by.',
    'past.',
    'around.',
    'concerning.',
    'regarding.',
    'with.',
    'at.',
    'despite.',
    'into.',
    'since.',
    'within.',
    'down.',
    'like.',
    'through.',
    'without.',
    'before.',
    'during.',
    'near.',
    'throughout.',
    'behind.',
    'of.',
    'to.'
]

# Take the users input.
with open('paperinput.txt') as f:
    text = f.readlines()

# Add all the lines together.
string = ''
for line in text:
    string += line + " "

# Do they end any sentences with a preposition?
words = string.lower().split()

# Make look nice. 
print('\n')

# Identify prepositions and surrounding words. 
count = 0
for word in words:
    if word in prepositions:
        if count >= 3:
            s = words[-3 + count] + ' ' + words[-2 + count] + ' ' + words[-1 + count] + ' ' + word    
        else:
            s = word        
        print(f'WARNING: Possible preposition at end of sentence?: {s}')
    count += 1
    
# Normalize the text.
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
print('\nYou used:')
for item, val in d:
    print(f'{item} : {val} times!')
