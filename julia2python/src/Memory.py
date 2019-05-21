"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
from LexicalAnalyzer import LexicalAnalyzer


class Memory:
    mem = [None] * 52

    def lookFor(self):
        return Memory.mem[Memory.getIndex(self)]

    def store(self, value):
        Memory.mem[Memory.getIndex(self)] = value

    def getIndex(ch):
        if not LexicalAnalyzer.is_valid_identifier(ch):
            raise ValueError(ch + " is not a valid identifier")
            print("The Identifier can only be one character")

        if ord(ch) - ord('A') < 26:
            return ord(ch) - ord('A')
        else:
            return ord(ch) - ord('a') + 26

    def clear():
        Memory.mem = [None] * 52
