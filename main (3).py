def SSL(a, k):
    return a << k

def SRL(a, k):
    return a >> k

def SLC(a):
    return ~a

def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def XOR(a, b):
    return a ^ b

def XNOR(a, b):
    return ~(a ^ b)

def IMPL(a, b):
    return (~a) | b

def flip(bit_string):
    return [not bit for bit in bit_string]

def flip_position(bit_string, position):
    bit_string[position] = not bit_string[position]
    return bit_string

a = 0b1010
b = 0b1100
print(SSL(a, 2)) 
print(SRL(b, 1)) 
print(SLC(a)) 
print(AND(a, b)) 
print(OR(a, b)) 
print(XOR(a, b)) 
print(XNOR(a, b)) 
print(IMPL(a, b)) 

bit_string = [True, False, True, False]
print(flip(bit_string)) 
print(flip_position(bit_string, 2))