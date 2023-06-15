from octalang.alphabet import to_group,letter_to_digit
from util import read_graphemes,is_alphanumeric,remove_successive_graphemes

# Take an Octalang text and translate it into natural text
def translate_from_octalang(text: str):
  if text == '':
    return ''
  chars = read_graphemes(text)
  digitized = ''.join([letter_to_digit(char) for char in chars])
  splits = digitized.split('/')
  octals = [split[1:-1].split(')(') for split in splits]
  chars = [[chr(int(octal,8)) for octal in group] for group in octals]
  return ' '.join([''.join(lexeme) for lexeme in chars])

# Take a natural text and translate it into Octalang text
def translate_to_octalang(text: str):
  if text == '':
    return ''
  chars = read_graphemes(text)
  text = []
  for char in chars:
    try:
      text.append(to_group(char) if is_alphanumeric(char) else '/')
    except TypeError:
      # Hacky solution for characters of too long length
      for c in char:
        text.append(to_group(c) if is_alphanumeric(char) else '/')
  text = ''.join(text)
  return remove_successive_graphemes(text,'/').strip('/')
