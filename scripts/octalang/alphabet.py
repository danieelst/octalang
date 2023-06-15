ALPHABET_DIGIT_DICT={'ɵ': '0',
                     'ọ': '1',
                     'o': '2',
                     'ô': '3',
                     'ǫ̂': '4',
                     'ộ': '5',
                     'ɵ̂': '6',
                     'ø̂': '7'}
ALPHABET_STR = 'ɵọoôǫ̂ộɵ̂ø̂'
ALPHABET=['ɵ','ọ','o','ô','ǫ̂','ộ','ɵ̂','ø̂']
OTHERS='()/'

# Translate an octal digit into an Octalang letter
def letter_to_digit(l: str):
  if l in ALPHABET_DIGIT_DICT:
    return ALPHABET_DIGIT_DICT[l]
  else:
    return l

# Translate an octal number into Octalang letters
def octal_to_letters(octal: str):
  return ''.join([ALPHABET[int(digit)] for digit in octal])

# Translate a letter into its octal value
def letter_to_octal(letter: str):
  # Example 'T' -> 84 -> 0o124 -> '124'
  return str(oct(ord(letter)))[2:]

# Translate a letter into an Octalang group
def to_group(letter: str):
  return '(' + octal_to_letters(letter_to_octal(letter)) + ')'
