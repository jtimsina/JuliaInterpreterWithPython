"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""

class ParserException(Exception):

    def __init__(self, JuliaCode):
        super(ParserException, self).__init__()
        print(JuliaCode + "\n")

