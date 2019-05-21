"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
from ArithmeticOperator import ArithmeticOperator


class BinaryExpression:

    def __init__(self, operator, expression_Node, expression_Node1):
        self.E1 = expression_Node
        self.E2 = expression_Node1
        self.Operator = operator

        if operator is None:
            raise ValueError("Null arithmetic operator argument")
        if expression_Node is None or expression_Node1 is None:
            raise ValueError("Null expression argument")


    def evaluate(self):
        Counter = 0
        if self.Operator == ArithmeticOperator.ADD_OP:
            Counter = self.E1.evaluate() + self.E2.evaluate()

        elif self.Operator == ArithmeticOperator.SUB_OP:
            Counter = self.E1.evaluate() - self.E2.evaluate()

        elif self.Operator == ArithmeticOperator.MUL_OP:
            Counter = self.E1.evaluate() * self.E2.evaluate()

        elif self.Operator == ArithmeticOperator.DIV_OP:
            Counter = self.E1.evaluate() / self.E2.evaluate()

        elif self.Operator == ArithmeticOperator.MOD_OP:
            Counter = self.E1.evaluate() % self.E2.evaluate()

        elif self.Operator == ArithmeticOperator.EXP_OP:
            Counter = self.E1.evaluate() ** self.E2.evaluate()

        elif self.Operator == ArithmeticOperator.REV_DIV_OP:
            Counter = self.E2.evaluate() / self.E1.evaluate()

        return Counter
