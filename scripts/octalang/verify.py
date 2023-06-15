from octalang.alphabet import ALPHABET,OTHERS
from util import read_graphemes

def valid_letters(text: str):
  return all([c in ALPHABET for c in read_graphemes(text) if c not in OTHERS])

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
