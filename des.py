
from des_algorithm import des_encrypt_block, des_decrypt_block
from BitVector import BitVector
from file_handling import write_to_file, read_from_file
import argparse
import base64

class DES:
    def __init__(self, agrs):
        self.args = agrs

    def handle_encrypttion(self):
        plainTextInput = read_from_file(self.args.arguments[0])
        keyInput = read_from_file(self.args.arguments[1])

        plainText = BitVector(textstring=plainTextInput)
        key = BitVector(textstring=keyInput)

        ciphertext = des_encrypt_block(plainText, key)

        #print(ciphertext.get_text_from_bitvector())
        write_to_file(self.args.arguments[2], ciphertext.get_bitvector_in_hex())

    def handle_decryption(self):
        cipherTextInput = read_from_file(self.args.arguments[0])
        keyInput = read_from_file(self.args.arguments[1])

        cipherText = BitVector(hexstring=cipherTextInput)
        key = BitVector(textstring=keyInput)

        decrypted = des_decrypt_block(cipherText, key)

        write_to_file(self.args.arguments[2], decrypted.get_text_from_bitvector())

    def run(self):
        
        if self.args.encryption:
            if len(self.args.arguments) != 3:
                print("Invalid number of arguments for encryption. Expected 3.")
                exit(1)
            self.handle_encrypttion()
        elif self.args.decryption:
            if len(self.args.arguments) != 3:
                print("Invalid number of arguments for decryption. Expected 3.")
                exit(1)
            self.handle_decryption()
        else:
            print("No mode selected. Exiting.")

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
    des = DES(args)
    des.run()
   
if __name__ == "__main__":
    main()