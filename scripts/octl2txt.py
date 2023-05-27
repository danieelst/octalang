import sys

ALPHABET_DICT={'ɵ':'0','ọ':'1','o':'2','ô':'3','ǫ̂':'4','ộ':'5','ɵ̂':'6','ø̂':'7'}
ALPHABET='ɵọoôǫ̂ộɵ̂ø̂'
OTHERS='()/'

def letter2digit(l: str):
  if l in ALPHABET_DICT:
    return ALPHABET_DICT[l]
  else:
    return l

# Take an Octalang string and turn it into a list of characters
# Note that some characters will be represented with two code points:
#   > ǫ̂: ǫ,^
#   > ɵ̂: ɵ,^
#   > ø̂: ø,^
def split_characters(text: str):
  i = len(text) - 1
  l = []
  while 0 <= i:
    if text[i] in ALPHABET_DICT or text[i] in OTHERS:
      l.insert(0,text[i])
    else:
      i -= 1
      l.insert(0,''.join([text[i],text[i+1]]))
    i -= 1
  return l

def translate(text: str):
  characters = split_characters(text)
  digitized = ''.join([letter2digit(char) for char in characters])
  splits = digitized.split('/')
  octals = [split[1:-1].split(')(') for split in splits]
  chars = [[chr(int(octal,8)) for octal in group] for group in octals]
  return ' '.join([''.join(lexeme) for lexeme in chars])

def valid_letters(text: str):
  return all([c in ALPHABET for c in text if c not in OTHERS])

# Check that brackets pair up and are not nested
def matching_brackets(text: str):
  brackets = [c for c in text if c == '(' or c == ')']
  l = []
  for i in range(0,len(brackets)):
    if len(l) > 1:
      return False # Nested brackets are not allowed
    elif brackets[i] == '(':
      l.append('(')
    else:
      if len(l) < 1:
        return False # Unmatched bracket
      else:
        l.pop()
  return len(l) == 0

def no_outer_splits(text: str):
  return text[0] != '/' and text[-1] != '/'

def no_empty_groups(text: str):
  return text.find('()') == -1

if __name__=='__main__':
  # Gather the input
  if len(sys.argv) > 1:
    text = ' '.join(sys.argv[1:])
  else:
    print('Provide text on the command line')
    sys.exit(-1)
  # Check validity of the string
  if not valid_letters(text):
    print('Invalid Octalang letters')
    sys.exit(-1)
  if not matching_brackets(text):
    print('Unmatched or nested brackets')
    sys.exit(-1)
  if not no_outer_splits(text):
    print('May not have outer splits')
    sys.exit(-1)
  if not no_empty_groups(text):
    print('May not have empty groups')
    sys.exit(-1)
  print(translate(text))
