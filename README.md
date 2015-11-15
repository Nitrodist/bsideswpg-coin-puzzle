# BSides Winnipeg 2015 Coin Puzzle

Ideas on what the ciphertext is:

* Base64 encdoded -- first four bytes are 78 9c after hexdumping which indicates 'Default compression' for zlib

How I generated `coin_text_base64_decoded.txt`:

```
cat coin_text_as_one_line.txt | base64 --decode > coin_text_base64_decoded.txt
```

## Bonus question or something?

On the badges, there's a 32 character code:

```
4dc357d7652464d4238a7543501045eb
```

This sequence could be used... as a decryption key? Whaaaaa???? This sequence looks strikingly like a md5 sum.

On the program, there's *another* 32 character code:

```
3e930a8b0cb5057027a6498265fbf67f
```

## Coin puzzle image
The puzzle image:

![Coin Puzzle Image](/coin.jpg?raw=true "Coin Puzzle Image")

