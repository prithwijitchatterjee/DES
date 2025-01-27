
from permutations import permute, IP, FP,E, P
from key_substitution import substitute
from generate_round_keys import generate_round_keys
from BitVector import BitVector

def feistel_function(right_half, subkey):
    # Expand the right half to 48bit
    expanded = permute(right_half, E)
    # XOR with the subkey
    xored = expanded ^ subkey
    # Substitute using S-boxes
    substituted = substitute(xored)
    # Permute the substituted bits with P boxes
    #print(f"Substituted: {substituted.size} {max(P)}")
    return permute(substituted, P)

def des_encrypt_block(block, key):
    """Encrypt a 64-bit block using DES."""
    #print (f"Block: {block.get_bitvector_in_hex()}")
    # TODO: need to uncomment the below code after adjusting the initial permutation
    #block = permute(block, IP)
    #print (f"Block after IP: {block.get_bitvector_in_hex()}")
    left, right = block.divide_into_two()
    subkeys = generate_round_keys(key)
    #print(f"Subkeys: {[subkey.get_bitvector_in_hex() for subkey in subkeys]}")
    for subkey in subkeys:
        #print(f"Left: {left.get_bitvector_in_hex()}, Right: {right.get_bitvector_in_hex()}")
        #print(f"Subkey: {subkey.get_bitvector_in_hex()} {max(subkey)} {right.size}")
        left, right = right, left ^ feistel_function(right, subkey)
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
