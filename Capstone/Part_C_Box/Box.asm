// Box.asm  --  K = 33
// Start row = 33  -> address SCREEN + 32*33 = 16384 + 1056 = 17440
// Width = 16 * ((33 mod 4) + 1) = 32 pixels = 2 words
// Height = 20 rows
// While any key is pressed: black box. Key released: box is cleared.

(LOOP)
    @KBD
    D=M
    @BLACK
    D;JNE           // key pressed -> black
    @color
    M=0             // no key -> white
    @DRAW
    0;JMP
(BLACK)
    @color
    M=-1            // all 16 bits = 1 -> black
(DRAW)
    @17440
    D=A
    @addr
    M=D             // addr = start of first row
    @20
    D=A
    @rows
    M=D             // rows = 20
(ROWLOOP)
    @2
    D=A
    @cols
    M=D             // cols = 2 words per row
    @addr
    D=M
    @p
    M=D             // p = current word address
(COLLOOP)
    @color
    D=M
    @p
    A=M
    M=D             // RAM[p] = color
    @p
    M=M+1
    @cols
    M=M-1
    D=M
    @COLLOOP
    D;JGT
    @32
    D=A
    @addr
    M=D+M           // next row (+32 words)
    @rows
    MD=M-1
    @ROWLOOP
    D;JGT
    @LOOP
    0;JMP