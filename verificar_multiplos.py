def verificar_multiplos(num1, num2):
    if num1 % num2 == 0:
        return f"{num1} es múltiplo de {num2}"
    elif num2 % num1 == 0:
        return f"{num2} es múltiplo de {num1}"
    else:
        return "Ninguno es múltiplo del otro"

# Ejemplo de uso
print(verificar_multiplos(7919, 2))
print(verificar_multiplos(840, 210))
print(verificar_multiplos(678223072849 , 23))
print(verificar_multiplos(1299827, 104729))
print(verificar_multiplos(104728, 13))