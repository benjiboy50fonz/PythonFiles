from palindrome_function import PalindromeTest

while True:
    word = raw_input('Enter a word or phrase: ')
    output = PalindromeTest(word)
    if not output:
        print('\nThis word is NOT a palindrome!\n')

    else:
        print('\nThis word is a palindrome!\n')

    continue

