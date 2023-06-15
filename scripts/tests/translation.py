from util import read_graphemes,is_alphanumeric,remove_successive_graphemes
from octalang.translate import translate_from_octalang,translate_to_octalang
from random import random,choice

# Pre-load all code points
all_code_points = [chr(i) for i in range(0,1114111+1)]
# Pre-load all alphanumeric code points
letters = [cp for cp in all_code_points if is_alphanumeric(cp)]
# Pre-load all non alphanumeric code points
others = [cp for cp in all_code_points if not is_alphanumeric(cp)]

def gen_natural_text(n_len: int):
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
def test_natural_to_natural(n_tests: int):
  # The original and the translation should be the same, except for
  # the replacement of non-alphanumerics with whitespace
  def compare(natural, translated):
    # Get all characters
    chars = read_graphemes(natural)
    natural = ''.join([c if is_alphanumeric(c) else ' ' for c in chars])
    natural = remove_successive_graphemes(natural, ' ').strip()
    res = natural == translated
    print(f'> "{natural}" == "{translated}": {res}')
    return res

  texts = [gen_natural_text(i) for i in range(1,n_tests)]
  translated = [translate_from_octalang(translate_to_octalang(text)) for text in texts]

  return all([compare(t1,t2) for (t1,t2) in zip(texts,translated)])
