# noinspection PyInterpreter
def calculateOppositeNA(start, data):
    if start == 'd':
        returnList = []
        # Provides sets of codons
        matches = {
            't': 'a',
            'a': 'u',
            'c': 'g',
            'g': 'c'
        }
        data = data.split()
        returnString = ''
        for codon in data:
            firstResult = matches[codon[0]]
            secondResult = matches[codon[1]]
            thirdResult = matches[codon[2]]
            returnList.append(str(firstResult + secondResult + thirdResult))
            returnString = (returnString + firstResult + secondResult + thirdResult + ' ').upper()
        return returnString, returnList
    # return string is RNA

    elif start == 'r':
        matches = {
            'a': 't',
            'u': 'a',
            'c': 'g',
            'g': 'c'
        }
        data = data.split()
        returnString = ''
        for codon in data:
            firstResult = matches[codon[0]]
            secondResult = matches[codon[1]]
            thirdResult = matches[codon[2]]
            returnString = (returnString + firstResult + secondResult + thirdResult + ' ').upper()
        return returnString
        # return string is DNA


def str(param):
    pass


def findAminoAcids(rna):
    # takes list with three vals
    code = {
        'gug': 'Valine',
        'gua': 'Valine',
        'guc': 'Valine',
        'guu': 'Valine',

        'gcg': 'Alanine',
        'gca': 'Alanine',
        'gcc': 'Alanine',
        'gcu': 'Alanine',

        'gau': 'Aspartic Acid',
        'gac': 'Aspartic Acid',
        'gaa': 'Glutamic Acid',
        'gag': 'Glutamic Acid',

        'ggu': 'Glycine',
        'ggc': 'Glycine',
        'gga': 'Glycine',
        'ggg': 'Glycine',

        'uug': 'Leucine',
        'uua': 'Leucine',
        'uuc': 'Phenylalanine',
        'uuu': 'Phenylalanine',

        'ucg': 'Serine',
        'uca': 'Serine',
        'ucc': 'Serine',
        'ucu': 'Serine',

        'uau': 'Tyrosine',
        'uac': 'Tyrosine',
        'uaa': 'Stop',
        'uag': 'Stop',

        'ugu': 'Cytesine',
        'ugc': 'Cytesine',
        'uga': 'Stop',
        'ugg': 'Tryptophan',

        'cug': 'Leucine',
        'cua': 'Leucine',
        'cuc': 'Leucine',
        'cuu': 'Leucine',

        'ccg': 'Proline',
        'cca': 'Proline',
        'ccc': 'Proline',
        'ccu': 'Proline',

        'cau': 'Histidine',
        'cac': 'Histidine',
        'caa': 'Glutamine',
        'cag': 'Glutamine',

        'cgu': 'Arginine',
        'cgc': 'Arginine',
        'cga': 'Arginine',
        'cgg': 'Arginine',

        'aug': 'Methionine',
        'aua': 'Isoleucine',
        'auc': 'Isoleucine',
        'auu': 'Isoleucine',

        'acg': 'Threonine',
        'aca': 'Threonine',
        'acc': 'Threonine',
        'acu': 'Threonine',

        'aau': 'Asparagine',
        'aac': 'Asparagine',
        'aaa': 'Lysine',
        'aag': 'Lysine',

        'agu': 'Serine',
        'agc': 'Serine',
        'aga': 'Arginine',
        'agg': 'Arginine'
    }
    aAList = ''
    for codon in rna:
        aa = code[str(codon.lower())]
        aAList = aAList + str(aa) + ' - '
    return aAList


print(
    '--------- \nBy Ben Bistline\n---------\n\nThis system requires DNA or RNA, and it will provide you with the '
    'other and Amino Acids!') 
DNAorRNA = True
while DNAorRNA:
    dOR = str(raw_input('\nDNA or RNA?: '))
    if str(dOR.lower()) == 'dna':
        originalInput = 'd'
        searchFor = ['t', 'a', 'c', 'g', ' ']
        break
    elif str(dOR.lower()) == 'rna':
        originalInput = 'r'
        searchFor = ['u', 'a', 'c', 'g', ' ']
        break
    else:
        print('\nInvalid answer!\n')
        continue
InvalidChar = True
while InvalidChar:
    givenData = str(raw_input('\nPlease enter your data in sets of three, separated by spaces!: ').lower())
    result = True
    for i in str(givenData):
        if str(i.lower()) not in searchFor:
            result = False
    if not result:
        print('Invalid character given! Maybe you\'re entering the wrong type?')
        continue
    InvalidChar = False

    if originalInput == 'd':
        RNA, RNAList = calculateOppositeNA(originalInput, givenData)
        aAList = findAminoAcids(RNAList)
        print('\nRNA: ' + str(RNA))
        print('Amino Acids: ' + str(aAList))

    else:
        DNA = calculateOppositeNA(originalInput, givenData)
        RNAForAA = givenData.split()
        aAList = findAminoAcids(RNAForAA)
        print('\nDNA: ' + str(DNA))
        print('Amino Acids: ' + str(aAList))
