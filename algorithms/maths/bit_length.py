def bit_length(n): # return the bit size of a non-negative integer
    if n == 0: return 0
    bits = -32
    m = 0
    while n:
        m = n
        n >>= 32; bits += 32
    while m: m >>= 1; bits += 1
    return bits
