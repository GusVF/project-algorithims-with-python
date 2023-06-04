def is_palindrome_iterative(word: str):
    listing = []
    if len(word) == 0:
        return False
    for i in range(len(word)):
        listing.append(word[i])
    listing.reverse()
    return ''.join(listing) == word


result = is_palindrome_iterative('tebet')
print(result)
