"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
class Iter:

    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
        self.iterator = ['']

        if expr1 is None or expr2 is None:
            raise ValueError("Null arithmetic expression argument")
            print("Problem in Arithmetic Expression")


    def evaluate(self):
        self.iterator.append(self.expr1.evaluate())
        self.iterator.append(self.expr2.evaluate())
        return self.iterator

