def lettersum(letters: str) -> int:
    '''Assign every lowercase letter a value, from 1 for a to 26 for z.
    Given a string of lowercase letters, find the sum of the values of the
    letters in the string.'''
    letter_values = ['', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    letter_sum = 0
    for letter in letters:
        letter_sum += letter_values.index(letter.lower())
    return letter_sum

def no_shared_letters(string_one, string_two):
    '''Find out if a pair of words have no letters in common'''
    set_one = set(string_one)
    set_two = set(string_two)
    return len(set_one.intersection(set_two)) > 0

print(no_shared_letters("cytotoxicity", "unreservedness"))

print(lettersum(""))
print(lettersum("a"))
print(lettersum("z"))
print(lettersum("cab"))
print(lettersum("excellent"))
print(lettersum("unreservedness"))
print(lettersum("microspectrophotometries"))
