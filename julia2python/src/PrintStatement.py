"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
class PrintStatement:

    def __init__(self, expression_node):
        super(PrintStatement, self).__init__()
        if expression_node is None:
            raise ValueError("Null arithmetic expression argument")

        self.expression = expression_node

    def execute(self):
        print(self.expression.evaluate())
