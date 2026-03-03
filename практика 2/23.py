import re

def calc(expression):
    """
    Принимает арифметическое выражение в виде строки (например, '1 + 9')
    и возвращает результат операции (сложение, вычитание, деление).
    """
   
    pattern = r'^\s*(-?\d+)\s*([+\-/*]?)\s*(-?\d+)\s*$'
    match = re.match(pattern, expression)
    
    if not match:
        return "Ошибка: неверный формат выражения"
    
    a_str, op, b_str = match.groups()
    a = float(a_str)
    b = float(b_str)
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        if b == 0:
            return "Ошибка: деление на ноль"
        return a / b
    else:
        return "Ошибка: неподдерживаемая операция (допустимы +, -, /)"

print(calc('1 + 9'))     
print(calc('15 - 4'))   
print(calc('20 / 5'))    

