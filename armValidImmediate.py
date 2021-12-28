#!/usr/bin/env python3


# Test whether an immediate value can be encoded by ARM32 Assembler by emulating the encoding mechanism

# chmod u+x ./armValidImmediate.py
# Usage: ./armValidImmediate.py [immediate-value-hex-or-dec-representation]

# v = n ror 2*r
# v - immediate value
# n - 8-bit immediate value (0-255)
# r - 4-bit rotational field (multiplied by 2 ) represents fields 0 - 30
# ref: https://azeria-labs.com/memory-instructions-load-and-store-part-4/

import sys

def rotate_right(input_byte, count, max_bits):
    input_byte = bin(input_byte).lstrip('0b')
    while(len(input_byte) < max_bits):
        input_byte = '0' + input_byte

    #110100_11 -> 11_110100
    input_byte = input_byte[max_bits - count:] + input_byte[:max_bits - count]
    return int(input_byte, base=2)

def main():
    if(len(sys.argv) != 2):
        print(f"usage: {sys.argv[0]} [immediate-test-value]")
        sys.exit(1)
    
    if(sys.argv[1].startswith('0x')):
        value = int(sys.argv[1], base=16)
    else:
        value = int(sys.argv[1])
    
    for n in range(0, 256):
        for r in range(0, 32, 2):
            if(rotate_right(n, r, 32) == value):
                print(f"{hex(value)} => {value} |  CAN be encoded as immediate")
                sys.exit(0)

    print("CANNOT be encoded as immedate")

if __name__ == '__main__':
    main()
