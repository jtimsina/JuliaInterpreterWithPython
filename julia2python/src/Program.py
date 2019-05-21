"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
class Program:

    def __init__(self, MainCode):
        if MainCode is None:
            raise ValueError("Null block argument")
            print("Please Check Your Julia code, No Block Detected")

        self.Block = MainCode

    def execute(self):
        self.Block.execute()
