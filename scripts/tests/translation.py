from util import read_graphemes,is_alphanumeric,remove_successive_graphemes
from octalang.translate import translate_from_octalang,translate_to_octalang
from random import random,choice
from string import printable

# Pre-load all code points
all_code_points = [chr(i) for i in range(0,1114111+1)]

def natural_reflective_translation(s: str):
  return translate_from_octalang(translate_to_octalang(s))

def output(str: str):
  print(f'> {str}')

def test_all_code_points():
  res = True
  for cp in all_code_points:
    translation = natural_reflective_translation(cp)
    if (is_alphanumeric(cp) and cp != translation) and \
       (not is_alphanumeric(cp) and '' != translation):
      res = False
      output(f'{cp}: Failed!')
  return res

# Only tests printable text
def gen_natural_text(n_len: int):
  letters = [cp for cp in printable if is_alphanumeric(cp)]
  others = [cp for cp in printable if not is_alphanumeric(cp)]
  text = ''
  chance = 0.3
  while len([cp for cp in text if is_alphanumeric(cp)]) < n_len:
    if random() < chance:
      text += choice(others)
      chance -= 0.1 # Prevent non-termination
    else:
      text += choice(letters)
      chance = 0.2
  return text

# Generate n strings of natural text: translate each to Octalang and back
def test_gen_natural_to_natural(n_tests: int):
  # The original and the translation should be the same, except for
  # the replacement of non-alphanumerics with whitespace
  def compare(natural, translated):
    # Get all characters
    chars = read_graphemes(natural)
    expected = ''.join([c if is_alphanumeric(c) else ' ' for c in chars])
    expected = remove_successive_graphemes(expected, ' ').strip()
    res = expected == translated
    output(f'"{natural}" => "{expected}": {res}')
    return res

  texts = [gen_natural_text(i) for i in range(1,n_tests)]
  translated = [translate_from_octalang(translate_to_octalang(text)) for text in texts]

  return all([compare(t1,t2) for (t1,t2) in zip(texts,translated)])

def test_natural_to_octalang(input_str: str, expected_str: str):
  translated = translate_to_octalang(input_str)
  res = translated == expected_str
  print(f'> "{input_str}" == "{expected_str}": {res}')
  return res
