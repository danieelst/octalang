from octalang.translate import translate_to_octalang
from util import read_cmd

def translate(text: str):
  return translate_to_octalang(text)

if __name__=='__main__':
  print(translate(read_cmd()))
