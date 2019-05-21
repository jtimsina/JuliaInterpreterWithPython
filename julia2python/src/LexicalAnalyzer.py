"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
from typing import TextIO
from TokenType import TokenType
from LexicalException import LexicalException
from Token import Token


class LexicalAnalyzer:

    def __init__(self, name):

        assert name is not None

        self.tokens = []
        file: TextIO

        with open(name, "r") as file:
            lines = file.readlines()
            lines = [x.strip() for x in lines]

        for y, line in enumerate(lines):
            self.read_lines(line, y)
        self.tokens.append(Token(y, 1, "EOS", TokenType.EOS_TOK))

    def read_lines(self, line, number):
        assert line is not None and number >= 0
        counter = 0

        counter = LexicalAnalyzer.skip_white_space(line, counter)

        while counter <= len(line)-1:
            lexeme = LexicalAnalyzer.get_lexeme(line, number, counter)
            token_type = LexicalAnalyzer.get_token_type(lexeme, number, counter)
            self.tokens.append(Token(number + 1, counter + 1, lexeme, token_type))
            counter += len(lexeme)
            counter = LexicalAnalyzer.skip_white_space(line, counter)

    def get_token_type(liexical, line_number, column_number): #this checks if it is a token
        assert liexical is not None and line_number >= 0 and column_number >= 0
        if liexical[0].isalpha():
            if len(liexical) == 1:
                if LexicalAnalyzer.is_valid_identifier(liexical[0]):
                    token_type = TokenType.ID_TOK

                else:
                    raise LexicalException(
                        "There is a Problem at row number {} and column {}".format(line_number + 1, column_number + 1))
            elif liexical == "if":
                token_type = TokenType.IF_TOK

            elif liexical == "function":
                token_type = TokenType.FUNCTION_TOK

            elif liexical == "end":
                token_type = TokenType.END_TOK

            elif liexical == "else":
                token_type = TokenType.ELSE_TOK

            elif liexical == "for":
                token_type = TokenType.FOR_TOK

            elif liexical == "while":
                token_type = TokenType.WHILE_TOK

            elif liexical == "print":
                token_type = TokenType.PRINT_TOK
            else:
                raise LexicalException(
                    "There is a problem at row number {} and column {}".format(line_number + 1, column_number + 1))
        elif liexical[0].isdigit():
            if LexicalAnalyzer.all_digits(liexical):
                token_type = TokenType.CONST_TOK
            else:
                raise LexicalException(
                    "Invalid liexical at row number {} and column {}".format(line_number + 1, column_number + 1))
        elif liexical == "+":
            token_type = TokenType.ADD_TOK

        elif liexical == "-":
            token_type = TokenType.SUB_TOK

        elif liexical == "*":
            token_type = TokenType.MUL_TOK

        elif liexical == "/":
            token_type = TokenType.DIV_TOK

        elif liexical == "\\":
            token_type = TokenType.REV_DIV_TOK

        elif liexical == "^":
            token_type = TokenType.EXP_TOK

        elif liexical == "%":
            token_type = TokenType.MOD_TOK

        elif liexical == "=":
            token_type = TokenType.ASSIGN_TOK

        elif liexical == "(":
            token_type = TokenType.LEFT_PAREN_TOK

        elif liexical == ")":
            token_type = TokenType.RIGHT_PAREN_TOK

        elif liexical == ">=":
            token_type = TokenType.GE_TOK

        elif liexical == ">":
            token_type = TokenType.GT_TOK

        elif liexical == "<=":
            token_type = TokenType.LE_TOK

        elif liexical == "<":
            token_type = TokenType.LT_TOK

        elif liexical == "==":
            token_type = TokenType.EQ_TOK

        elif liexical == "!=":
            token_type = TokenType.NE_TOK

        elif liexical == ":":
            token_type = TokenType.COL_TOK
        else:
            raise LexicalException(
                "Invalid liexical at row number {} and column {}".format(line_number + 1, column_number + 1))
        return token_type

    def all_digits(self):
        assert self is not None
        i = 0
        while i < len(self) and self[i].isdigit():
            i += 1
        return i == len(self)

    def get_lexeme(line, line_number, index):
        assert line is not None and line_number >= 0 and index >= 0
        i = index
        while i < len(line):
            if line[i].isspace():
                break
            i += 1
        return line[index:i]

    def skip_white_space(line, index):
        assert line is not None and index >= 0
        i = index
        while i < len(line):
            if not line[i].isspace():
                break
            i += 1
        return i

    def get_next_token(self):
        if not len(self.tokens):
            raise LexicalException("No more tokens")
            print("")
        return self.tokens.pop(0)

    def get_lookahead_token(self):
        if not len(self.tokens):
            raise LexicalException("No more tokens")
            print("")
        return self.tokens[0]

    def is_valid_identifier(self):
        return self.isalpha()
