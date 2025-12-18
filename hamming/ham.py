def xor(a, b):
    return int(a)^int(b)

def encode_hamming_block(data_bits):
    d = [int(b) for b in data_bits]

    p1 = xor(xor(d[0], d[1]), d[3]) 
    p2 = xor(xor(d[0], d[2]), d[3]) 
    p3 = xor(xor(d[1], d[2]), d[3]) 

    codeword = [p1, p2, d[0], p3, d[1], d[2], d[3]]
    return "".join(map(str, codeword))

def encode_hamming_string(binary_string):
    
    while len(binary_string) % 4 != 0:
        binary_string += '0'
    
    encoded_string = ""
    for i in range(0, len(binary_string), 4):
        block = binary_string[i:i+4]
        encoded_string += encode_hamming_block(block)
        
    return encoded_string

def decode_hamming_block(codeword_bits):

    c = [int(b) for b in codeword_bits]

    s1 = xor(xor(xor(c[0], c[2]), c[4]), c[6]) 
    s2 = xor(xor(xor(c[1], c[2]), c[5]), c[6]) 
    s3 = xor(xor(xor(c[3], c[4]), c[5]), c[6]) 

    error = (s3 << 2) | (s2 << 1) | s1
    
    return error

def decode_hamming_string(encoded_string):
    if len(encoded_string) % 7 != 0:
        return "Ошибка: длина строки не кратна 7."

    for i in range(0, len(encoded_string), 7):
        block = encoded_string[i: i + 7]
        error_in_block = decode_hamming_block(block)
        
        if error_in_block != 0:
            absolute_error_index = i + error_in_block
            return absolute_error_index 

    return -1 


