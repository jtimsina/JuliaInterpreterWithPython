"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
from RelativeOperator import RelativeOperator


class BooleanExpression:

    def __init__(self, BooleanOperator, expression, expression1):
        self.BooleanOperator = BooleanOperator
        self.boolean_expression = expression
        self.boolean_expression1 = expression1

        if self.BooleanOperator is None:
            raise ValueError("Null relative operator argument")
        if expression is None or expression1 is None:
            raise ValueError("Null arithmetic expression argument")

    def evaluate(self):
        boolean = False
        if self.BooleanOperator == RelativeOperator.LE_OP:
            boolean = self.boolean_expression.evaluate() <= self.boolean_expression1.evaluate()
        elif self.BooleanOperator == RelativeOperator.LT_OP:
            boolean = self.boolean_expression.evaluate() < self.boolean_expression1.evaluate()
        elif self.BooleanOperator == RelativeOperator.GE_OP:
            boolean = self.boolean_expression.evaluate() >= self.boolean_expression1.evaluate()
        elif self.BooleanOperator == RelativeOperator.GT_OP:
            boolean = self.boolean_expression.evaluate() > self.boolean_expression1.evaluate()
        elif self.BooleanOperator == RelativeOperator.EQ_OP:
            boolean = self.boolean_expression.evaluate() == self.boolean_expression1.evaluate()
        elif self.BooleanOperator == RelativeOperator.NE_OP:
            boolean = self.boolean_expression.evaluate() != self.boolean_expression1.evaluate()
        return boolean
