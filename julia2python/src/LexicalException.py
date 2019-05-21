"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
class LexicalException(Exception):

    def __init__(self, string):
        super(LexicalException, self).__init__()
        print(string + "\n")
