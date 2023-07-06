def fibonacci_recursivo(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

# Exemplo de uso:
n = 9
resultado = fibonacci_recursivo(n)
print(f"F({n}) = {resultado}")
