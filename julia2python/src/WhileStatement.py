"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
class WhileStatement:

    def __init__(self, expression, block):

        self.Expression = expression
        self.Block = block

        if self.Expression is None:
            raise ValueError("Null boolean expression argument")
            print("While loop is missing Expression")
        if self.Block is None:
            raise ValueError("Null block argument")
            print("While loop is Missing its block")


    def execute(self):
        while self.Expression.evaluate():
            self.Block.execute()
            print("Executing while block")
