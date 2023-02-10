import main;

def test1():
    assert main.simple_calculator("add", 5, 4) == 9
def test2():
    assert main.simple_calculator("multiply", 19, 15) == 285
def test3():
    assert main.simple_calculator("division", 9, 0) == "ZeroDivisionError"
