
from des_algorithm import des_encrypt_block, des_decrypt_block,des_encrypt_image
from BitVector import BitVector
from file_handling import read_ppm_image_file, write_to_file, read_from_file, write_bitvector_to_file, copy_ppm_header
import argparse
import base64

class DES:
    def __init__(self, agrs):
        self.args = agrs

    def handle_encrypttion(self):
        plainTextInput = read_from_file(self.args.arguments[0])
        keyInput = read_from_file(self.args.arguments[1])

        # # Pad plaintext to be a multiple of 8 bytes
        # padded_plaintext = pad_plaintext(plainTextInput.encode())
        # vector_plaintext = BitVector(rawbytes=padded_plaintext)
        # key= BitVector(textstring=keyInput)

        ciphertext = des_encrypt_block(plainTextInput, keyInput)

        #print(ciphertext)
        write_to_file(self.args.arguments[2], ciphertext.get_hex_string_from_bitvector())

    def handle_decryption(self):
        cipherTextInput = read_from_file(self.args.arguments[0])
        keyInput = read_from_file(self.args.arguments[1])
        
        decrypted = des_decrypt_block(cipherTextInput, keyInput)
        write_to_file(self.args.arguments[2], decrypted.get_text_from_bitvector())

    def handle_image_encrypt(self):
        #copy the source file to the destination file with the header
        copy_ppm_header(self.args.arguments[0], self.args.arguments[2])

        plainTextInput = read_ppm_image_file(self.args.arguments[0])
        keyInput = read_from_file(self.args.arguments[1])

        #plainText = BitVector(rawbytes=plainTextInput)
        #key = BitVector(textstring=keyInput)

        ciphertext = des_encrypt_image(plainTextInput, keyInput)
        write_bitvector_to_file(self.args.arguments[2], ciphertext)

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
        elif self.args.imgencryption:
            if len(self.args.arguments) != 3:
                print("Invalid number of arguments for image encryption. Expected 3.")
                exit(1)
            self.handle_image_encrypt()
        else:
            print("No mode selected. Exiting.")

def main():
    parser = argparse.ArgumentParser(description="Process some input arguments.")

    # Define flags
    parser.add_argument("-e", "--encryption", action="store_true", help="Encryoption mode")
    parser.add_argument("-d", "--decryption", action="store_true", help="Decryption mode")
    parser.add_argument("-i", "--imgencryption", action="store_true", help="Decryption mode")
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