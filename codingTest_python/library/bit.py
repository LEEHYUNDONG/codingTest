bit = 0b1001

print(bin(~(0b001000)))
print(bin(0b10100110 & 0b11011111))  # AND
print(bin(0b1010 | 0b0101))  # OR
print(bin(0b0000 ^ 0b1100))  # XOR
print(bin(0b0110 << 2))  # shift 2 to the left,
print(bin(0b0110 >> 2))  # shift right twice

# 원소 추가
n = 3
print(bin(0b0010 | (1 << n)))
print(bin(0b0010 | (1 << 2)))

# 원소 제거
n = 3
print(bin(0b1010 & ~(1 << n)))  # 0b10

# 조회
n = 2
print(bin(0b1010 & (1 << n)))  # 0b1000
