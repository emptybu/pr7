def solve_equation(a, b, c):
    return a * b + 4 * c

try:
    print(f"Уравнениe: x = a * b + 4 * c")
    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    c = float(input("Введите значение c: "))
    x = solve_equation(a, b, c)
    print(f"Решение уравнения: x = {x}")
except ValueError:
    print("Ошибка: введите корректные числовые значения.")
    
