# ILHAM8 CPU EMULATOR

This is an 8-bit cpu emulator with a custom instruction set
coded in python

## Registers 
```
00 - reg a
01 - reg b
10 - reg c
11 - reg d
```

## Instruction set
### ALU Instructions
All answers are stored in the first register provided.
For example: `AND 00 01` would store the result in register a or '00'

**And:**

> And is a simple bitwise and function that can be performed on 2 registers
> using the syntax `AND X Y`, with x and y being the binary identifiers of 
> any register.

**Or / Xor:**

> These are both simple bitwise functions that can be performed on 2 registers using 
> the syntax `OR X Y` or `XOR X Y`.

**Not:**

> This is a not function that uses the syntax `NOT X`.

**Add / Sub:**

> This is a function that adds/subtracts 2 registers (`ADD X Y`/`SUB X Y`).

**Shr / Shl:**

> Shift right/left. Shifts the value of a register right or left by one bit place Use the syntax `SHR X`/`SHL X`.

### Jump Functions

**Jmp:**

> Jump without a condition. `JMP Z`(Z representing an 8-bit address)

**Jc / Jnc:**

> Jump (not) carry jumps depending on the state of the carry flag (`J(N)C Z`)

**Jp / Jn:**

> Jump based on the state of the negative flag (Jp if false and Jn if True)(`J* Z`)

**Je / Jne:**

> Jump based on the state of the equal flag using syntax `J(N)E Z`

**Jpe / Jpo:**

> Jump based on the state of the parity flag (Jpe for true and Jpo for false)(`JP* Z`)

**Cmp:**

> Compares 2 Regisers and sets the equal flag to either True or False. (`CMP X Y`)

### RAM loading functions

**Load:**

> Load a specific piece of data to a register. (`LOAD X A` Where a is an 8-bit binary number)

**Str:**

> Store a register value to a specific RAM address. (`STR X Z`)

**Print:**

> Output a register value to the CLI. (`PRINT X`)

**Inp:**

> Store a user input to a register. (`INP X`)

## Compiling a .ilh file

Run the compiler and input the name of your .ilh file (including the extension).
The compiler will output a .ilhbin file (Name unchanged) to the same folder. To
recompile, firs remove the .ilhbin file and run again.

## Emulating a .ilhbin file

When you run the emulator, input your filename (with extension) and it will run. If your file is more than 255 lines long, some RAM addresses will be inaccessable, 
due to limitations of 8 bit systems.

## Using Test Programs
In the folder [`./examples/bin`](https://github.com/IlhamIbrahimli/Ilham8/tree/main/examples/bin) 
will be .ilhbin files that are labelled with what they do.
The source code for these files is available in the 
[`./examples/asm`](https://github.com/IlhamIbrahimli/Ilham8/tree/main/examples/asm)
folder. It will contain
.ilh files. (When creating a .ilh file please do not use full stops in the filename otherwise
the compiler will not use the full name when naming the .ilhbin file.)
