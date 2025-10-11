def conversor_fahrenheit(celsius: float) -> float:
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def conversor_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) / 1.8
    return celsius


