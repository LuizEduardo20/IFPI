def celsius(fahrenheit):
    return ((fahrenheit - 32) / 9) * 5

def test_celsius():
    assert celsius(32) == 0
    assert celsius(212) == 100
    assert abs(celsius(98.6) - 37) < 0.1
    
    print("Todos os testes passaram!")

test_celsius()