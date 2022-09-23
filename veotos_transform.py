from string import ascii_lowercase

VOWELS_LOWERCASE = 'aeiou'
CONSONANTS_LOWERCASE = ''.join(
    [letter for letter in ascii_lowercase if letter not in VOWELS_LOWERCASE]
)
ACUTE_VOWELS_LOWERCASE = 'áéíóú'
UMLAUT_VOWELS_LOWERCASE = 'äëïöü'

GROUPS_TO_TRANSFORM = []
GROUPS_TO_TRANSFORM.append(VOWELS_LOWERCASE)
GROUPS_TO_TRANSFORM.append(CONSONANTS_LOWERCASE)
GROUPS_TO_TRANSFORM.append(ACUTE_VOWELS_LOWERCASE)
GROUPS_TO_TRANSFORM.append(UMLAUT_VOWELS_LOWERCASE)

# Add uppercase letters
for group in GROUPS_TO_TRANSFORM.copy():
    GROUPS_TO_TRANSFORM.append(group.upper())


def wrapping_slice(string, start):
    """
    Given a :string return another string beginning at :start:
        wrapping around the length of the :string:.

    Visualize this:
        Glue the beginning and the end of the given :string: and go to
        position given by :start: to make a cut there to get a list again.
    """
    return ''.join([string[i % len(string)]
                    for i in range(start, len(string) + start)])


def find_new_text(text, iteration):
    """
    Returns the new text that will substitute every consonant or vowel
    from the ASCII characters with the next iteration-th consonant or vowel.
    """
    for value in GROUPS_TO_TRANSFORM:
        code = (f"table = ''.maketrans('{value}', "
                f"wrapping_slice('{value}',{iteration}))")
        exec(code, globals())
        text = text.translate(table)
    return text


if __name__ == "__main__":
    for i in range(len(VOWELS_LOWERCASE)*len(CONSONANTS_LOWERCASE)+1):
        print(find_new_text('Taisir Avilés', i))
