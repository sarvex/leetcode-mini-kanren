class Solution:
    def add(self, a: int, b: int) -> int:
        a, b = a & 0xFFFFFFFF, b & 0xFFFFFFFF
        while b:
            c = ((a & b) << 1) & 0xFFFFFFFF
            a, b = a ^ b, c
        return a if a < 0x80000000 else ~(a ^ 0xFFFFFFFF)
