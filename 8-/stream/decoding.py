

def decode(eqution: dict) -> str:
    new_equation = []
    for key, value in eqution.items():
        if value != 0:
            new_equation.append(f'{value}*x**{key}')
    new_equation = ' + '.join(new_equation) + ' = 0'
    new_equation = new_equation.replace('+ -', '- ')\
        .replace(' 1*x', ' x').replace('*x**0', '').replace('x**1', 'x')
    
    return new_equation