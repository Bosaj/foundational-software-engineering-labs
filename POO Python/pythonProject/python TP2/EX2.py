def addition(a, b):
    return a + b
def soustraction(a, b):
    return a - b
def multiblication(a,b):
    return a * b
def division(a, b):
    if b == 0:
        raise ValueError("Division par zéro impossible")
    return a / b