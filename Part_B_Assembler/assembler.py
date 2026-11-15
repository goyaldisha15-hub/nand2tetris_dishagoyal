# ---------- A-INSTRUCTION ----------

def a_instruction(command):
    number = int(command[1:])
    binary = format(number, '016b')
    return binary


# ---------- C-INSTRUCTION TABLES ----------

comp_table = {
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "M":   "1110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "!M":  "1110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "-M":  "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101"
}


dest_table = {
    "null": "000",
    "M":    "001",
    "D":    "010",
    "MD":   "011",
    "A":    "100",
    "AM":   "101",
    "AD":   "110",
    "AMD":  "111"
}


jump_table = {
    "null": "000",
    "JGT":  "001",
    "JEQ":  "010",
    "JGE":  "011",
    "JLT":  "100",
    "JNE":  "101",
    "JLE":  "110",
    "JMP":  "111"
}


# ---------- C-INSTRUCTION ----------

def c_instruction(command):
    dest = "null"
    jump = "null"

    if "=" in command:
        dest, command = command.split("=")

    if ";" in command:
        comp, jump = command.split(";")
    else:
        comp = command

    return (
        "111"
        + comp_table[comp]
        + dest_table[dest]
        + jump_table[jump]
    )

def assemble_file(input_file, output_file):
    machine_code = []

    with open(input_file, "r") as file:
        for line in file:
            # Comments aur blank lines remove karo
            line = line.split("//")[0].strip()

            if not line:
                continue

            if line.startswith("@"):
                binary = a_instruction(line)

            else:
                binary = c_instruction(line)

            machine_code.append(binary)

    with open(output_file, "w") as file:
        for instruction in machine_code:
            file.write(instruction + "\n")

    print("Assembly completed!")
    print("Output saved in:", output_file)


if __name__ == "__main__":
    assemble_file("test.asm", "test.hack")

