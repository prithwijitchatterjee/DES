
from permutations import permute, IP, FP,E, P
from key_substitution import substitute
from generate_round_keys import generate_round_keys
from BitVector import BitVector
from log import log

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

def des_encrypt_block(block, key):
    """Encrypt a 64-bit block using DES."""
    # TODO: need to uncomment the below code after adjusting the initial permutation
    #block = permute(block, IP)
    #print (f"Block after IP: {block.get_bitvector_in_hex()}")
    left, right = block.divide_into_two()
    log(f"First block of plaintext represented as a BitVector:  Left Block: {left.get_bitvector_in_hex()}, Right Block: {right.get_bitvector_in_hex()}")
    subkeys = generate_round_keys(key)
    for index, subkey in enumerate(subkeys):
        left, right = right, left ^ feistel_function(right, subkey, 1==1)
    #return permute(right + left, FP)
    return right + left

def des_decrypt_block(block, key):
    """Decrypt a 64-bit block using DES."""
    #block = permute(block, IP)
    left, right = block.divide_into_two()
    subkeys = generate_round_keys(key)[::-1]
    for subkey in subkeys:
        left, right = right, left ^ feistel_function(right, subkey)
    #return permute(right + left, FP)
    return right + left
