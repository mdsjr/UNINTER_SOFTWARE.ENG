# FIBONACCI RECURSIVO
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

n = 3

resultado = fibonacci_recursivo(n)
print(f"F({n}) = {resultado}")