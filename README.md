# 🐙 Octalang 📜

Octalang is a constructed language which adopts every other language. It does this by converting a source text's characters' values (á la Unicode) into octal numerals, where each digit corresponds to a letter in Octalang. Thus, Octalang inherits the source language's grammar and lexicon. Therefore, every language is considered as a dialect of Octalang.

```
ᴴᵉˡˡᵒ ᵂᵒʳˡᵈ ᵉˣᵃᵐᵖˡᵉ
(ọọɵ)(ọǫ̂ộ)(ọộǫ̂)(ọộǫ̂)(ọộø̂)/(ọoø̂)(ọộø̂)(ọɵ̂o)(ọộǫ̂)(ọǫ̂ǫ̂)
```

The full specification is given in `paper.pdf`.

## Scripts

Translating to Octalang:

```
python3 txt2octl.py <text>
```

Translating from Octalang:

```
python3 octl2txt.py <text>
```

The scripts are developed to be completely stand-alone.

PSA: Make sure that you have enabled a font that can properly display the characters (e.g. Consolas).

## Documenation

`paper.pdf` is generated from `paper.tex` using Overleaf and the XeLaTeX compiler.
