
from des_algorithm import des_encrypt_block, des_decrypt_block
from BitVector import BitVector
from file_handling import write_to_file, read_from_file
import argparse
import base64

def handle_encrypttion(args):
    plainTextInput = read_from_file(args.arguments[0])
    keyInput = read_from_file(args.arguments[1])

    plainText = BitVector(textstring=plainTextInput)
    key = BitVector(textstring=keyInput)

    ciphertext = des_encrypt_block(plainText, key)

    #print(ciphertext.get_text_from_bitvector())
    write_to_file(args.arguments[2], ciphertext.get_bitvector_in_hex())

def handle_decryption(args):
    cipherTextInput = read_from_file(args.arguments[0])
    keyInput = read_from_file(args.arguments[1])

    cipherText = BitVector(hexstring=cipherTextInput)
    key = BitVector(textstring=keyInput)

    decrypted = des_decrypt_block(cipherText, key)

    write_to_file(args.arguments[2], decrypted.get_text_from_bitvector())

def main():
    parser = argparse.ArgumentParser(description="Process some input arguments.")

    # Define flags
    parser.add_argument("-e", "--encryption", action="store_true", help="Encryoption mode")
    parser.add_argument("-d", "--decryption", action="store_true", help="Decryption mode")
    # Add positional arguments for all unnamed inputs
    parser.add_argument(
        "arguments",
        nargs="*",
        help="All additional unnamed arguments"
    )

    # Parse the arguments
    args = parser.parse_args()
    
    # Use the flags
    if args.encryption:
        print("Encryption...")
        if len(args.arguments) != 3:
            print("Invalid number of arguments for encryption. Expected 3.")
            exit(1)
        handle_encrypttion(args)
    
    if args.decryption:
        print("Decryption...")
        if len(args.arguments) != 3:
            print("Invalid number of arguments for decryption. Expected 3.")
            exit(1)
        handle_decryption(args)
    
    if not (args.encryption or args.decryption):
        print("No mode selected. Exiting.")

   
if __name__ == "__main__":
    main()