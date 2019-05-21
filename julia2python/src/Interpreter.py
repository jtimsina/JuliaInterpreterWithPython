"""
Zave Timsina, Xiaoju Jiang, Andrea Pinardi
Kuruba Senigala, Ramesh
Concept of programming language section 02
10/29/2018

"""
from Memory import Memory
from Parser import Parser

if __name__ == '__main__':

    files = ["julia1.txt"]
    JuliaCode = "julia1.txt"
    parser = Parser(JuliaCode)
    print('Executing...----------------------------------------------------\n')
    print(format(JuliaCode))
    print('\bOutput')
    intrepret = parser.parse()
    intrepret.execute()

    Memory.clear()
    print('Test Complete.. No error')

"""
JUlIA Code Samples to Copy and Paste in Julia.txt file

Code 1

function a ( )
x = 1
while <= x 3
print ( x )
 x = + x 1
end
print ( 9999 )
end

code 2

function b ( )
x = 1
y = 1
a = % x   y
z = + x   y
print ( z )
print ( a )
end


code 3 

function c ( )
x = 1
if < x 2
print ( x )
else
print ( * x 2 )  
end
end
  
"""