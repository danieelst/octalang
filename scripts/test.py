from tests.translation import test_gen_natural_to_natural,test_natural_to_octalang

def test(res: bool):
  if res:
    print('Passed!')
  else:
    print('Failed!')

if __name__=='__main__':
  print('-- Testing translation of generated strings --')
  test(test_gen_natural_to_natural(200))
  print('-- Testing translation of strings --')
  test(test_natural_to_octalang('Hello World',
    '(ọọɵ)(ọǫ̂ộ)(ọộǫ̂)(ọộǫ̂)(ọộø̂)/(ọoø̂)(ọộø̂)(ọɵ̂o)(ọộǫ̂)(ọǫ̂ǫ̂)'))
  test(test_natural_to_octalang('A constructed language',
    '(ọɵọ)/(ọǫ̂ô)(ọộø̂)(ọộɵ̂)(ọɵ̂ô)(ọɵ̂ǫ̂)(ọɵ̂o)(ọɵ̂ộ)(ọǫ̂ô)(ọɵ̂ǫ̂)(ọǫ̂ộ)(ọǫ̂ǫ̂)/(ọộǫ̂)(ọǫ̂ọ)(ọộɵ̂)(ọǫ̂ø̂)(ọɵ̂ộ)(ọǫ̂ọ)(ọǫ̂ø̂)(ọǫ̂ộ)'))
