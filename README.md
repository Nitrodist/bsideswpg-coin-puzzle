# BSides Winnipeg 2015 Coin Puzzle

## Step 1 - base64 decode ciphertext

Transcribe from the coin, the ciphertext (check `coin_text_as_one_line.txt` if you don't want to do that):

```
cat coin_text_as_one_line.txt | base64 --decode > coin_text_base64_decoded.txt
```

## Step 2 - convert ciphertext to qr code (draw the rest of the owl)

Notice that the ciphertext has only nibbles in it: F 0 3 C. Check it out by doing this:

```
python decompress_zlib.py | hexdump -C
```

Which produces this:

```
00000000  ff fc 33 cf ff ff ff 0c  f3 ff fc 00 cf c0 c0 0f  |..3.............|
00000010  00 33 f0 30 03 cf cc 3f  0c fc f3 f3 0f c3 3f 3c  |.3.0...?......?<|
00000020  fc cc f0 cf cf 3f 33 3c  33 f3 cf cc 3f cc fc f3  |.....?3<3...?...|
00000030  f3 0f f3 3f 3c 00 cc c0  c0 0f 00 33 30 30 03 ff  |...?<......300..|
00000040  fc cc cf ff ff ff 33 33  ff f0 00 03 0c 00 00 00  |......33........|
00000050  00 c3 00 00 ff cf f0 f3  33 3f f3 fc 3c cc c0 f0  |........3?..<...|
00000060  3c 30 c3 0c 3c 0f 0c 30  c3 0f cf c3 0f cf 03 f3  |<0..<..0........|
00000070  f0 c3 f3 c0 0f 30 0c cf  cc 03 cc 03 33 f3 33 cc  |.....0......3.3.|
00000080  ff 0c c3 0c f3 3f c3 30  c0 00 0f 3c c0 cc 00 03  |.....?.0...<....|
00000090  cf 30 33 ff fc fc 33 ff  3f ff 3f 0c ff cc 00 c3  |.03...3.?.?.....|
000000a0  cf f3 f3 00 30 f3 fc fc  cf cc c3 ff 00 33 f3 30  |....0........3.0|
000000b0  ff c0 0c fc cc 3c 0f f3  3f 33 0f 03 fc cf cc fc  |.....<..?3......|
000000c0  00 f0 33 f3 3f 00 3c 0c  00 cf f0 fc c3 00 33 fc  |..3.?.<.......3.|
000000d0  3f 30 ff fc ff 33 f3 3f  ff 3f cc fc c0 0a        |?0...3.?.?....|
000000de
```

Say that they translate to these sequences based on binary:

* `F: 1111`
* `0: 0000`
* `3: 0011`
* `C: 1100`

Let's clean up the output a bit:

```
python decompress_zlib.py | hexdump | perl -pe 's!^........?!!g' | perl -pe 's! !!g'
fffc33cfffffff0cf3fffc00cfc0c00f
0033f03003cfcc3f0cfcf3f30fc33f3c
fcccf0cfcf3f333c33f3cfcc3fccfcf3
f30ff33f3c00ccc0c00f0033303003ff
fccccfffffff3333fff000030c000000
00c30000ffcff0f3333ff3fc3cccc0f0
3c30c30c3c0f0c30c30fcfc30fcf03f3
f0c3f3c00f300ccfcc03cc0333f333cc
ff0cc30cf33fc330c0000f3cc0cc0003
cf3033fffcfc33ff3fff3f0cffcc00c3
cff3f30030f3fcfccfccc3ff0033f330
ffc00cfccc3c0ff33f330f03fccfccfc
00f033f33f003c0c00cff0fcc30033fc
3f30fffcff33f33fff3fccfcc00a
00000de
```

Convert the F, C, 3, and 0s to 1's and 0's:

```
python decompress_zlib.py | hexdump | perl -pe 's!^........?!!g' | perl -pe 's! !!g' | sed 's!X!█!g' | sed 's!\.! !g' | sed 's!f!██!g' | sed 's!c! █!g' | sed 's!3! █!g' | sed 's!0!  !g'
██████ █ █ █ ███████████████   ███ ███████ █     ███ █   █    ██
     █ ███   █     █ ███ █ █ ███   ███ ███ ███ █  ██ █ █ ███ █ █
██ █ █ ███   ███ ███ ███ █ █ █ █ █ ███ █ ███ █ █ ███ █ ███ ███ █
██ █  ████ █ ███ █ █     █ █ █   █    ██     █ █ █   █     █████
██ █ █ █ ███████████████ █ █ █ ███████         █   █
     █ █        ████ █████  ██ █ █ █ █████ ███ █ █ █ █ █ █  ██
 █ █ █   █ █   █ █ █  ██   █ █   █ █  ██ ███ █ █  ██ ███   ███ █
██   █ ███ █ █    ██ █     █ ███ █ █   █ █ █   █ █ ███ █ █ █ █ █
████   █ █ █   ███ █ ███ █ █ █   █        ██ █ █ █   █ █       █
 ███ █   █ ███████ ███ █ █ █████ ███████ ███   █████ █ █     █ █
 █████ ███ █     █  ██ ███ ███ █ ███ █ █ █ █████     █ ███ █ █
████ █     ███ █ █ █ █ █  ████ █ ███ █ █  ██   ███ █ ███ █ ███ █
    ██   █ ███ █ ███     █ █   █     █████  ██ █ █ █     █ ███ █
 ███ █  ██████ █████ █ ███ █ ███████ ███ █ ███ █ █    a
```

Looks weird, doesn't it? OK, let's assume that the image is *square*. What's the nearest square of the characters we have now? Here's how we did it (used 'X's instead of `█` in this case):

```
python decompress_zlib.py | hexdump | perl -pe 's!^........?!!g' | perl -pe 's! !!g'     | sed 's!f!XXXX!g' | sed 's!c!XX  !g' | sed 's!3!  XX!g' | sed 's!0!    !g' | tr -d '\n' | wc -c
1773
```

Let's dump the characters to a file (`qr_without_newlines.txt`) so that we can use it more easily:

```
python decompress_zlib.py | hexdump | perl -pe 's!^........?!!g' | perl -pe 's! !!g'     | sed 's!f!████!g' | sed 's!c!██  !g' | sed 's!3!  ██!g' | sed 's!0!    !g' | tr -d '\n' > qr_without_newlines.txt
```

The nearest square root of `1773` is `42`.  So let's make an image based on newlines after 42 characters:

```
cat qr_without_newlines.txt | ruby -e 'ARGF.read.each_char.with_index{|char, i| if i % 42 == 0; print "\n"; end; print char }'


██████████████    ██  ████  ██████████████
██████████████    ██  ████  ██████████████
██          ██  ██████      ██          ██
██          ██  ██████      ██          ██
██  ██████  ██    ██████    ██  ██████  ██
██  ██████  ██    ██████    ██  ██████  ██
██  ██████  ██  ██  ████    ██  ██████  ██
██  ██████  ██  ██  ████    ██  ██████  ██
██  ██████  ██    ████████  ██  ██████  ██
██  ██████  ██    ████████  ██  ██████  ██
██          ██  ██  ██      ██          ██
██          ██  ██  ██      ██          ██
██████████████  ██  ██  ██  ██████████████
██████████████  ██  ██  ██  ██████████████
                  ██    ██
                  ██    ██
██████████  ████████    ████  ██  ██  ██
██████████  ████████    ████  ██  ██  ██
    ████      ████    ██    ██    ██    ██
    ████      ████    ██    ██    ██    ██
    ██████  ██████    ██    ██████  ████
    ██████  ██████    ██    ██████  ████
        ████  ██        ██  ██  ██████  ██
        ████  ██        ██  ██  ██████  ██
  ██  ████  ██  ████████    ██  ██    ██
  ██  ████  ██  ████████    ██  ██    ██
                ████  ████  ██      ██  ██
                ████  ████  ██      ██  ██
██████████████  ██████    ██  ██████████
██████████████  ██████    ██  ██████████
██          ██    ████  ████████  ██████
██          ██    ████  ████████  ██████
██  ██████  ██  ██    ██████████
██  ██████  ██  ██    ██████████
██  ██████  ██  ██    ████      ████████
██  ██████  ██  ██    ████      ████████
██  ██████  ██  ██████          ████
██  ██████  ██  ██████          ████
██          ██  ████████    ██████  ██
██          ██  ████████    ██████  ██
██████████████  ████████  ██  ██████  ██
██████████████  ████████  ██  ██████  ██
        a
```

Looks like a QR code! Let's set our terminal up to display it better so that we can use a QR scanner on our phone to scan it.

Adjust the foreground and background color:

![Adjust FG and BG colors in terminal](/adjust-fg-and-bg-color.jpg?raw=true "Adjust FG and BG colors in terminal")

Adjust vertical spacing:

![Adjust vertical spacing](/vertical-spacing.jpg?raw=true "Adjust vertical spacing")

Here's the result!

![Result of terminal adjustments](/result.jpg?raw=true "Result of termainl adjustments")



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

