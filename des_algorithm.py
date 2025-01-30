
from permutations import permute, IP, FP,E, P
from key_substitution import substitute
from generate_round_keys import generate_round_keys
from BitVector import BitVector
from log import log

# Pad plaintext with zeros if not a multiple of 8 bytes
def pad_plaintext(plaintext):
    padding_length = 8 - (len(plaintext) % 8)
    return plaintext + (b'\x00' * padding_length)

# Remove zero padding after decryption
def unpad_plaintext(padded_plaintext):
    return padded_plaintext.rstrip(b'\x00')

def feistel_function(right_half, subkey, logFlag=False):
    # Expand the right half to 48bit
    expanded = permute(right_half, E)
    if(logFlag):
        log("First block of plaintext after expansion permutation in round 1/16")
        log(f"Right Block (hex): {expanded.get_bitvector_in_hex()}")
    # XOR with the subkey
    xored = expanded ^ subkey
    if(logFlag):
        log("First block of plaintext after XOR with subkey in round 1/16")
        log(f"Right Block (hex): {xored.get_bitvector_in_hex()}")
    # Substitute using S-boxes
    substituted = substitute(xored)
    if(logFlag):
        log("First block of plaintext after substitution using S-boxes in round 1/16")
        log(f"Right Block (hex): {substituted.get_bitvector_in_hex()}")
    # Permute the substituted bits with P boxes
    permuted = permute(substituted, P)
    if(logFlag):
        log("First block of plaintext after permutation using P-boxes in round 1/16")
        log(f"Right Block (hex): {permuted.get_bitvector_in_hex()}")
    return permuted

def des_encrypt_image(plaintext, key):
    
    # Generate Subkeys    
    key_bv = BitVector(textstring=key)
    subkeys = generate_round_keys(key_bv)

    ciphertext_blocks = BitVector(size=0)

    print(f"Length of plaintext: {len(plaintext)}")

    for i in range(0, len(plaintext), 64):  # 64 bits
        block = block = BitVector(rawbytes=plaintext[i:i+64])
        left, right = block.divide_into_two()

        for index, subkey in enumerate(subkeys):
            left, right = right, left ^ feistel_function(right, subkey, index==0)
        output = right + left
        ciphertext_blocks += output
        
    return ciphertext_blocks

def des_encrypt_block(plaintext, key):
    
    # Generate Subkeys
    key_bv = BitVector(textstring=key)
    subkeys = generate_round_keys(key_bv)

    # Pad plaintext to be a multiple of 8 bytes
    padded_plaintext = pad_plaintext(plaintext.encode())
    ciphertext_blocks = BitVector(size=0)

    for i in range(0, len(padded_plaintext), 8):
        block = BitVector(rawbytes=padded_plaintext[i:i+8])
        left, right = block.divide_into_two()
        log(f"{i}th First block of plaintext represented as a BitVector:  Left Block: {left.get_bitvector_in_hex()}, Right Block: {right.get_bitvector_in_hex()}")
        
        for index, subkey in enumerate(subkeys):
            left, right = right, left ^ feistel_function(right, subkey, index==0)
        output = right + left       
        ciphertext_blocks += output
        
    return ciphertext_blocks
   
def des_decrypt_block(ciphertext, key):
    
    # Generate Subkeys
    key_bv = BitVector(textstring=key)
    subkeys = generate_round_keys(key_bv)

    ciphertext_blocks = BitVector(size=0)

    for i in range(0, len(ciphertext), 16):  # 16 hex chars = 64 bits
        block = BitVector(hexstring=ciphertext[i:i+16])
        left, right = block.divide_into_two()

        for subkey in reversed(subkeys):
            left, right = right, left ^ feistel_function(right, subkey)
        
        output = right+left
        ciphertext_blocks += output


    return ciphertext_blocks