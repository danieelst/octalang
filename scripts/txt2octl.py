import sys

ALPHABET=['ɵ','ọ','o','ô','ǫ̂','ộ','ɵ̂','ø̂']

def char2octal(c: str):
  # Example 'T' -> 84 -> 0o124 -> '124'
  return str(oct(ord(c)))[2:]

def octal2letters(octal: str):
  return ''.join([ALPHABET[int(digit)] for digit in octal])

def translate_char(c: str):
  return '(' + octal2letters(char2octal(c)) + ')'

def translate(text: str):
  text = ''.join([translate_char(c) if c.isalpha() else '/' for c in text])
  return text.strip('/')

if __name__=='__main__':
  # Gather the input
  if len(sys.argv) > 1:
    text = ' '.join(sys.argv[1:])
  else:
    print('Provide text on the command line')
    sys.exit(-1)
  print(translate(text))
