def PalindromeTest(word):
    final_string = str(word.lower())
    reverse_string = final_string[::-1]  # type: str
    if final_string == reverse_string:
        return True
    else:
        return False
