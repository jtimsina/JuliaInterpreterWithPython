"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""

class Block:

    def __init__(self):
        self.statement_nodes = []

    def add(self, StatementNode):
        if StatementNode is None:
            raise ValueError("Null statement argument")
            print("Check if Statement")

        self.statement_nodes.append(StatementNode)

    def execute(self):
        for x in self.statement_nodes:
            x.execute()
