# BSides Winnipeg 2015 Coin Puzzle

Ideas on what the ciphertext is:

* Base64 encdoded -- first four bytes are 78 9c after hexdumping which indicates 'Default compression' for zlib

How I generated `coin_text_base64_decoded.txt`:

```
cat coin_text_as_one_line.txt | base64 --decode > coin_text_base64_decoded.txt
```

The puzzle image:

![Coin Puzzle Image](/coin.jpg?raw=true "Coin Puzzle Image")

