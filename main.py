import random
import string

excluded_chars = set("AEIOULS015")
allowed_chars = [c for c in string.ascii_uppercase + string.digits if c not in excluded_chars]

def generate_code(length=25, chunk_size=5):
    raw_code = ''.join(random.choices(allowed_chars, k=length))
    return '-'.join(raw_code[i:i+chunk_size] for i in range(0, length, chunk_size))

def generate_multiple_codes(count=5, length=25, chunk_size=5):
    codes = set()
    while len(codes) < count:
        codes.add(generate_code(length, chunk_size))
    return list(codes)

if __name__ == "__main__":
    # Default settings
    num_codes = 5
    code_length = 25
    chunk_size = 5

    codes = generate_multiple_codes(num_codes, code_length, chunk_size)

    for idx, code in enumerate(codes, start=1):
        print(f"Code {idx}: {code}")
