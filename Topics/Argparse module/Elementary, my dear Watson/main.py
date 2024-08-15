import argparse

# Insert your decode_caesar_cipher function here
def decode_caesar_cipher(s, n):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print(text)

# Write your parser here
parser = argparse.ArgumentParser(description="This program decodes the given word with the specified offset and prints"
                                             "the result.")
parser.add_argument("--word")
parser.add_argument("--offset", type=int)

# Parse the Arguments
args = parser.parse_args()

# Call the decode function with the parsed arguments
decode_caesar_cipher(args.word, -args.offset)