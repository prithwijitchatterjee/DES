def write_to_file(file_path, data):
    with open(file_path, 'w', encoding="utf-8") as file:
        file.write(data)

def write_bitvector_to_file(file_file, bitvector):
    # Open the file in binary write mode
    with open(file_file, 'ab') as file:
        bitvector.write_to_file(file)

def read_from_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return file.read()

def copy_ppm_header(source_file, output_file):
    with open(source_file, 'rb') as src, open(output_file, 'wb') as dst:
        # Read and write the magic number
        magic_number = src.readline()
        dst.write(magic_number)

        # Read and write header lines (dimensions, max color value)
        while True:
            line = src.readline()
            dst.write(line)
            # Stop after writing the max color value
            if not line.startswith(b"#") and line.strip().isdigit():
                break

def read_ppm_image_file(file_path):
    with open(file_path, 'rb') as file:
        # Skip the magic number line
        file.readline()
        
        # Skip comments and header lines
        while True:
            line = file.readline()
            if not line.startswith(b"#"):  # Skip comments
                break
        
        # Read dimensions (width and height)
        while b"#" in line:
            line = file.readline()
        dimensions = line.strip()
        width, height = map(int, dimensions.split())
        
        # Skip the max color value line
        file.readline()
        
        # Read raw pixel data
        image_data = file.read()  # Binary RGB data for each pixel
        
        return image_data
