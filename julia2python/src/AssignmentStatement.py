"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
from Memory import Memory


class AssignmentStatement:

    def __init__(self, Data_Type, Expression_Node):
        if Data_Type is None:
            raise ValueError("Null Id argument")
        if Expression_Node is None:
            raise ValueError("Null ArithmeticExpression argument")
        self.Expression_Node = Expression_Node
        self.Data_Type = Data_Type

    def execute(self):
        Memory.store(self.Data_Type.get_char(), self.Expression_Node.evaluate())
