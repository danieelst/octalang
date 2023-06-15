from tests.translation import test_natural_to_natural

def test(res: bool):
  if res:
    print('Passed!')
  else:
    print('Failed!')

if __name__=='__main__':
  print('-- Testing translation of strings --')
  test(test_natural_to_natural(200))
