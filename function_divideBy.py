''''
Apython program that divides  two numbers
Exception error handling when you divide a number by 0
'''
def divide(a,b):
    if b==0:
        raise ValueError('Cannot divide by zero')
    return a/b
try:
    print(divide(100,0))
except ValueError as e:
    print("Error",e)
except Exception as e:
    print("Unknown Error occured ".e)
