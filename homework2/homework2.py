def decimal_to_binary(decimal):
    return bin(decimal)[2:]

def decimal_to_octal(decimal):
    return oct(decimal)[2:]

decimal_number = int(input("Введите десятичное число: "))
binary_result = decimal_to_binary(decimal_number)
octal_result = decimal_to_octal(decimal_number)

print(f"Двоичное представление: {binary_result}")
print(f"Восьмеричное представление: {octal_result}")
