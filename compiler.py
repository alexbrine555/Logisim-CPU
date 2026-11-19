reg = {"r0": 0b0000,
       "r1": 0b0001,
       "r2": 0b0010,
       "r3": 0b0011,
       "r4": 0b0100,
       "r5": 0b0101,
       "r6": 0b0110,
       "r7": 0b0111,
       "r8": 0b1000,
       "r9": 0b1001,
       "r10": 0b1010,
       "r11": 0b1011,
       "r12": 0b1100,
       "r13": 0b1101,
       "r14": 0b1110,
       "r15": 0b1111}
tokens = []
final = str()
f = open(r".\computer\src.txt")
r = open(r".\computer\bin.txt", "w")
def regs(a):
    b = hex(reg[a])[2:]
    return b
def dec2hex(a):
    b = hex(int(a))[2:]
    if len(b) != 2:
        b = "0" + b
    return b
def addr2hex(a):
    b = hex(int(a))[2:]
    while len(b) < 3:
        b = "0" + b
    return b
def branch(a, b):
    ab = str()
    match a:
        case 'zero':
            ab += "01"
        case 'carry':
            ab += "10"
        case 'carryzero':
            ab += "11"
        case 'none':
            ab += "00"
    ab += b
    c = addr2hex(int(ab))
    return c
lines = f.read()    
tokens = lines.split()
print(tokens)
for i in range(len(tokens)):
    match tokens[i]:
        case 'ldi':
            final += "a"
            i+=1
            final += regs(tokens[i])
            i+=1
            final += dec2hex(tokens[i])
        case 'not':
            final += "1"
            i+=1
            final += regs(tokens[i])
            final += "0"
            i+=1
            final += regs(tokens[i])
        case 'ret':
            final += "2"
            final += "000"
        case "xor":
            final += "4"
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
        case "nor":
            final += "3"
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
        case "and":
            final += "5"
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
        case "call":
            final += "6"
            i+=1
            final += addr2hex(tokens[i])
        case "add":
            final += "7"
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
        case "subtract":
            final += "8"
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
        case "rsh":
            final += "9"
            i+=1
            final += regs(tokens[i])
            final += "0"
            i+=1
            final += regs(tokens[i])
        case "nop":
            final += "0000"
        case "adi":
            final += "b"
            i+=1
            final += regs(tokens[i])
            i+=1
            final += dec2hex(tokens[i])
        case "hlt": 
            final += "f000"
        case "jmp":
            final += "c"
            i+=1
            final += addr2hex(tokens[i])
        case "branch":
            final += "d"
            i+=1
            final += branch(tokens[i], tokens[i+1])
            i+=1
        case "lod":
            final += "1"
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
            i+=1
            final += hex(int(tokens[i]))[2:]
        case "str":
            final += "e"
            i+=1
            final += regs(tokens[i])
            i+=1
            final += regs(tokens[i])
            i+=1
            final += hex(int(tokens[i]))[2:]
r.write(final)
print(final)
f.close()
r.close()