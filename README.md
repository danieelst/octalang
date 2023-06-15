# 🐙 Octalang 📜

Octalang is a constructed language which adopts every other language. It does this by converting a source text's characters' values (á la Unicode) into octal numerals, where each digit corresponds to a letter in Octalang. Thus, Octalang inherits the source language's grammar and lexicon. Therefore, every language is considered as a dialect of Octalang.

Wihtout further ado, here is `"Hello World"` in Octalang:

```
(ọọɵ)(ọǫ̂ộ)(ọộǫ̂)(ọộǫ̂)(ọộø̂)/(ọoø̂)(ọộø̂)(ọɵ̂o)(ọộǫ̂)(ọǫ̂ǫ̂)
```

The full specification is given in `paper.pdf`.

## Scripts

Translating to Octalang:

```
python3 scripts/txt2octl.py <text>
```

Translating from Octalang:

```
python3 scripts/octl2txt.py <text>
```

PSA: Make sure that you have enabled a font that can properly display the characters (e.g. Consolas).

There are also two scripts for simple echoing:
  * `octl2octl.py`: takes Octalang text, translates to natural text, and back to Octalang text
  * `txt2txt.py`: takes natural text, translates to Octalang text, and back to natural text

## Documentation

`paper.pdf` is generated from `paper.tex` using Overleaf and the XeLaTeX compiler.
