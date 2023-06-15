import sys

from octalang import verify
from octalang.translate import translate_from_octalang

from util import read_cmd

def translate(text: str):
  # Check validity of the string
  if not verify.valid_letters(text):
    print('Invalid Octalang letters')
    sys.exit(-1)
  if not verify.matching_brackets(text):
    print('Unmatched or nested brackets')
    sys.exit(-1)
  if not verify.no_outer_splits(text):
    print('May not have outer splits')
    sys.exit(-1)
  if not verify.no_empty_groups(text):
    print('May not have empty groups')
    sys.exit(-1)
  return translate_from_octalang(text)

if __name__=='__main__':
  print(translate(read_cmd()))
