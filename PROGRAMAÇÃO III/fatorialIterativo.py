#Fatorial iterativo
def fatorial_iterativo(n):
    fat = 1
    if n < 0:
        return None
    elif n== 0 or n== 1:
        return fat
    else:
        for i in range(1, n+1):
            fat *= i
        return fat
    
print(fatorial_iterativo(5))


""""
def fatorial_iterativo(n): - Aqui estamos definindo uma função chamada "fatorial_iterativo" que recebe um número "n" como entrada. Essa função calcula o fatorial desse número.

fat = 1 - Criamos uma variável chamada "fat" e a inicializamos com o valor 1. Essa variável será usada para armazenar o resultado do fatorial.

if n < 0: - Verificamos se o valor de "n" é menor que zero (um número negativo). Se for, retornamos "None", o que indica que o fatorial não pode ser calculado para números negativos.

elif n == 0 or n == 1: - Se a condição anterior não for satisfeita, verificamos se "n" é igual a zero ou igual a um. Se for, isso significa que o fatorial de zero ou um é igual a um, então retornamos o valor atual de "fat".

else: - Se nenhuma das condições anteriores for satisfeita, entramos nesse bloco else, o que significa que "n" é um número positivo maior que um.

for i in range(1, n+1): - Iniciamos um loop for que itera de 1 até o valor de "n+1". Ou seja, o loop vai percorrer todos os números de 1 até "n".

fat *= i - Dentro do loop, multiplicamos o valor atual de "fat" pelo valor atual de "i". Essa operação acumula o produto dos números de 1 até "n" em "fat".

return fat - Após o loop, retornamos o valor final de "fat", que é o fatorial de "n".

print(fatorial_iterativo(5)) - Chamamos a função "fatorial_iterativo" passando o valor 5 como argumento. Em seguida, imprimimos o resultado retornado pela função, que é o fatorial de 5.
"""