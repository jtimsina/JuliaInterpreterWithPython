"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
from TokenType import TokenType
from ArithmeticOperator import ArithmeticOperator
from AssignmentStatement import AssignmentStatement
from BinaryExpression import BinaryExpression
from Block import Block
from BooleanExpression import BooleanExpression
from Constant import Constant
from ForStatement import ForStatement
from Id import Id
from IfStatement import IfStatement
from Iter import Iter
from LexicalAnalyzer import LexicalAnalyzer
from PrintStatement import PrintStatement
from Program import Program
from RelativeOperator import RelativeOperator
from WhileStatement import WhileStatement


class Parser:

    def __init__(self, file_name):
        self.lex = LexicalAnalyzer(file_name)

    def parse(self):
        token = self.lex.get_next_token()
        Parser.match(token, TokenType.FUNCTION_TOK)
        function_Name = self.get_id()
        token = self.lex.get_next_token()
        Parser.match(token, TokenType.LEFT_PAREN_TOK)
        token = self.lex.get_next_token()
        Parser.match(token, TokenType.RIGHT_PAREN_TOK)
        block = self.get_block()
        token = self.lex.get_next_token()
        Parser.match(token, TokenType.END_TOK)
        token = self.lex.get_next_token()
        if token.get_tok_type() != TokenType.EOS_TOK:
            raise Exception("File has Garbage")
            print("There is extra information on the julia")
        return Program(block)

    def get_block(self):
        new_block = Block()
        new_token = self.lex.get_lookahead_token()
        while Parser.is_valid_start_of_statement(new_token):
            statement = self.get_statement()
            new_block.add(statement)
            new_token = self.lex.get_lookahead_token()
        return new_block

    def get_statement(self):
        statement_token = self.lex.get_lookahead_token()
        if statement_token.get_tok_type() == TokenType.IF_TOK:
            statement_node = self.get_if_statement()

        elif statement_token.get_tok_type() == TokenType.WHILE_TOK:
            statement_node = self.get_while_statement()

        elif statement_token.get_tok_type() == TokenType.PRINT_TOK:
            statement_node = self.get_print_statement()

        elif statement_token.get_tok_type() == TokenType.ID_TOK:
            statement_node = self.get_assignment_statement()

        elif statement_token.get_tok_type() == TokenType.FOR_TOK:
            statement_node = self.get_for_statement()
        else:
            raise Exception(
                "invalid statement at row " + tok.get_row_number() + " and column " + tok.get_column_number())
        return statement_node

    def get_assignment_statement(self):
        Data_type = self.get_id()
        assignment_token = self.lex.get_next_token()
        expression_inStatement = self.get_arithmetic_expression()
        Parser.match(assignment_token, TokenType.ASSIGN_TOK)

        return AssignmentStatement(Data_type, expression_inStatement)

    def get_print_statement(self):
        print_statement_token = self.lex.get_next_token()
        Parser.match(print_statement_token, TokenType.PRINT_TOK)

        print_statement_token = self.lex.get_next_token()
        Parser.match(print_statement_token, TokenType.LEFT_PAREN_TOK)

        expression_inPrint = self.get_arithmetic_expression()
        print_statement_token = self.lex.get_next_token()
        Parser.match(print_statement_token, TokenType.RIGHT_PAREN_TOK)
        return PrintStatement(expression_inPrint)

    def get_if_statement(self):
        ifStatement_token = self.lex.get_next_token()
        Parser.match(ifStatement_token, TokenType.IF_TOK)
        ifStatement_expression = self.get_boolean_expression()
        ifstatement_block = self.get_block()
        ifStatement_token = self.lex.get_next_token()
        Parser.match(ifStatement_token, TokenType.ELSE_TOK)
        ifstatement_block1 = self.get_block()
        ifStatement_token = self.lex.get_next_token()
        Parser.match(ifStatement_token, TokenType.END_TOK)
        return IfStatement(ifStatement_expression, ifstatement_block, ifstatement_block1)

    def get_for_statement(self):
        for_statement_token = self.lex.get_next_token()
        Parser.match(for_statement_token, TokenType.FOR_TOK)
        Data_Type_Forstm = self.get_id()
        for_statement_token = self.lex.get_next_token()
        Parser.match(for_statement_token, TokenType.ASSIGN_TOK)
        expression_ForStatement = self.get_arithmetic_expression()
        for_statement_token = self.lex.get_next_token()
        Parser.match(for_statement_token, TokenType.COL_TOK)
        expression_forStatement1 = self.get_arithmetic_expression()
        forStatement_block = self.get_block()
        for_statement_token = self.lex.get_next_token()
        Parser.match(for_statement_token, TokenType.END_TOK)
        iterator = Iter(expression_ForStatement, expression_forStatement1)
        return ForStatement(Data_Type_Forstm, iterator, forStatement_block)

    def get_while_statement(self):
        while_statement_token = self.lex.get_next_token()
        Parser.match(while_statement_token, TokenType.WHILE_TOK)
        whileStatement_expression = self.get_boolean_expression()
        while_statement_block = self.get_block()
        while_statement_token = self.lex.get_next_token()
        Parser.match(while_statement_token, TokenType.END_TOK)
        return WhileStatement(whileStatement_expression, while_statement_block)

    def is_valid_start_of_statement(validToken):
        assert (validToken is not None)
        return validToken.get_tok_type() == TokenType.ID_TOK or validToken.get_tok_type() == TokenType.IF_TOK \
               or validToken.get_tok_type() == TokenType.WHILE_TOK or validToken.get_tok_type() == TokenType.FOR_TOK \
               or validToken.get_tok_type() == TokenType.PRINT_TOK

    def get_arithmetic_expression(self):
        Arithmetic_token = self.lex.get_lookahead_token()
        if Arithmetic_token.get_tok_type() == TokenType.ID_TOK:
            arithmetic_expression = self.get_id()
        elif Arithmetic_token.get_tok_type() == TokenType.CONST_TOK:
            arithmetic_expression = self.get_constant()
        else:
            arithmetic_expression = self.get_binary_expression()
        return arithmetic_expression   # returns arthimetic expresson

    def get_binary_expression(self):
        binary_expression_Token = self.lex.get_next_token()
        if binary_expression_Token.get_tok_type() == TokenType.ADD_TOK:
            Parser.match(binary_expression_Token, TokenType.ADD_TOK)
            Binary_operator = ArithmeticOperator.ADD_OP

        elif binary_expression_Token.get_tok_type() == TokenType.SUB_TOK:
            Parser.match(binary_expression_Token, TokenType.SUB_TOK)
            Binary_operator = ArithmeticOperator.SUB_OP

        elif binary_expression_Token.get_tok_type() == TokenType.MUL_TOK:
            Parser.match(binary_expression_Token, TokenType.MUL_TOK)
            Binary_operator = ArithmeticOperator.MUL_OP

        elif binary_expression_Token.get_tok_type() == TokenType.DIV_TOK:
            Parser.match(binary_expression_Token, TokenType.DIV_TOK)
            Binary_operator = ArithmeticOperator.DIV_OP

        elif binary_expression_Token.get_tok_type() == TokenType.REV_DIV_TOK:
            Parser.match(binary_expression_Token, TokenType.REV_DIV_TOK)
            Binary_operator = ArithmeticOperator.REV_DIV_OP

        elif binary_expression_Token.get_tok_type() == TokenType.EXP_TOK:
            Parser.match(binary_expression_Token, TokenType.EXP_TOK)
            Binary_operator = ArithmeticOperator.EXP_OP

        elif binary_expression_Token.get_tok_type() == TokenType.MOD_TOK:
            Parser.match(binary_expression_Token, TokenType.MOD_TOK)
            Binary_operator = ArithmeticOperator.MOD_OP
        else:
            raise Exception(
                " operator expected at row " + binary_expression_Token.get_row_number() + " and column " + binary_expression_Token.get_column_number())
            print("Operator Missing")
        Binary_expression = self.get_arithmetic_expression()
        Binary_expression1 = self.get_arithmetic_expression()
        return BinaryExpression(Binary_operator, Binary_expression, Binary_expression1)  #returns binary expression

    def get_boolean_expression(self):
        Boolean_Token = self.lex.get_next_token()
        if Boolean_Token.get_tok_type() == TokenType.EQ_TOK:
            operator = RelativeOperator.EQ_OP

        elif Boolean_Token.get_tok_type() == TokenType.NE_TOK:
            operator = RelativeOperator.NE_OP

        elif Boolean_Token.get_tok_type() == TokenType.GT_TOK:
            operator = RelativeOperator.GT_OP

        elif Boolean_Token.get_tok_type() == TokenType.GE_TOK:
            operator = RelativeOperator.GE_OP

        elif Boolean_Token.get_tok_type() == TokenType.LT_TOK:
            operator = RelativeOperator.LT_OP

        elif Boolean_Token.get_tok_type() == TokenType.LE_TOK:
            operator = RelativeOperator.LE_OP
        else:
            raise Exception("relational operator expected at row " + Boolean_Token.get_row_number() + " and column " + Boolean_Token.get_column_number())
            print("Operator missing")
        Boolean_expression = self.get_arithmetic_expression()
        Boolean_expression1 = self.get_arithmetic_expression()
        return BooleanExpression(operator, Boolean_expression, Boolean_expression1)

    def get_id(self):
        IdToken = self.lex.get_next_token()
        Parser.match(IdToken, TokenType.ID_TOK)
        return Id(IdToken.get_lexeme()[0])

    def match(Token, type):
        assert (Token is not None and type is not None)
        if Token.get_tok_type() != type:
            raise Exception(
                type.name() + " expected at row " + Token.get_row_number() + " and column " + Token.get_column_number())
            print("Token " + type.name() + " missing")

    def get_constant(self):
        Token_Node = self.lex.get_next_token()
        Parser.match(Token_Node, TokenType.CONST_TOK)
        x = int(Token_Node.get_lexeme())
        return Constant(x)

