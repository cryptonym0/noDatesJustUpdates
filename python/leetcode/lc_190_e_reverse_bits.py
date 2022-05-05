class Solution:
    def reverseBits(self, n: int) -> int:
        # ok
        # I can do this
        # i remeber sharma making me do this by hand
        # I am the algorithm
        length = 32
        binary = bin(n)[2:].rjust(length, "0")[::-1]
        return int(binary, 2)
        # holy shit


#         i = 0
#         for b in n:
#             i = i**2 + int(b)
