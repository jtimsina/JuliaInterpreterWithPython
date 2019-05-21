"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
class Token:

    def __init__(self, x, y, Lex, type):

        self.x = x
        self.y = y
        self.type = type
        self.lex = Lex

        if x <= 0:
            raise Exception("IllegalArgumentException")
            print("Invalid row")

        if y <= 0:
            raise Exception("IllegalArgumentException")
            print("Invalid column")

        if Lex is None or 0 == len(Lex):
            raise Exception("IllegalArgumentException")
            print("Not Lexical analyzer")

        if type is None:
            raise Exception("IllegalArgumentException")
            print("Token Type Problem")

    def get_row_number(self):
        return self.x

    def get_column_number(self):
        return self.y

    def get_lexeme(self):
        return self.lex

    def get_tok_type(self):
        return self.type

