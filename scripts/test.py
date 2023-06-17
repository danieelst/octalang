from tests.translation import (test_all_code_points,
                               test_gen_natural_to_natural,
                               test_natural_to_octalang)

from literals import LITERALS

def test(res: bool):
  if res:
    print('Passed!')
  else:
    print('Failed!')

if __name__=='__main__':
  print('-- Testing translation of all code points --')
  test(test_all_code_points())
  print('-- Testing translation of generated strings --')
  test(test_gen_natural_to_natural(20))
  print('-- Testing translation of strings --')
  for nat,octl in LITERALS.items():
    test(test_natural_to_octalang(nat,octl))
