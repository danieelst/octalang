import sys
import regex

# Find all graphemes in a string, return as a list
def read_graphemes(s: str):
  return regex.findall(r'\X',s)

# Test if a character is either alphabetic or a digit
def is_alphanumeric(c: str):
  return c.isalpha() or c.isdigit()

# If a grapheme appears in succession, reduce it to only a single instance
def remove_successive_graphemes(s: str, c: str):
  return regex.sub(f'{c}+',c,s)

# Read command-line argument
def read_cmd():
  # Gather the input
  if len(sys.argv) > 1:
    text = ' '.join(sys.argv[1:])
  else:
    print('Provide text on the command line')
    sys.exit(-1)
  return text
