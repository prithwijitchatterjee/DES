from BitVector import BitVector

# Initial Permutation Tables
IP = [56,48,40,32,24,16,8,0,57,49,41,33,25,17,
      9,1,58,50,42,34,26,18,10,2,59,51,43,35,
      62,54,46,38,30,22,14,6,61,53,45,37,29,21,
      13,5,60,52,44,36,28,20,12,4,27,19,11,3]

# Final permutation table
FP = [39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25,
      32, 0, 40, 8, 48, 16, 56, 24]

# Expansion table
E =  [31,  0,  1,  2,  3,  4,
      3,  4,  5,  6,  7,  8,
      7,  8,  9, 10, 11, 12,
      11, 12, 13, 14, 15, 16,
      15, 16, 17, 18, 19, 20,
      19, 20, 21, 22, 23, 24,
      23, 24, 25, 26, 27, 28,
      27, 28, 29, 30, 31,  0]

# Permutation table
P = [15, 6, 19, 20, 28, 11, 27, 16,
     0, 14, 22, 25, 4, 17, 20, 9,
     1, 7, 23, 13, 31, 26, 2, 8,
     18, 12, 29, 5, 21, 10, 3, 24]

def permute(bitvector, table):
    """Permute a BitVector using a table."""
    return bitvector.permute(table)

# def permute(bitvector, list):
#     """Permute a BitVector using a table."""
#     return bitvector.permute(list)
