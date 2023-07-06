#Fatorial Recursivo
def fatorial_recursivo(n):
    fat = 1
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return fat
    else:
        return n * fatorial_recursivo(n-1)

print(fatorial_recursivo(5))
'''''
def fatorial_recursivo(n):

Aqui estamos definindo uma função chamada fatorial_recursivo que recebe um parâmetro n.
Essa função calcula o fatorial de n de forma recursiva.
fat = 1

Cria uma variável fat e atribui o valor 1 a ela.
Essa variável será usada para calcular o fatorial.
if n < 0:

Verifica se o valor de n é menor que 0.
Se for, retorna None indicando um valor inválido para o cálculo do fatorial.
elif n == 0 or n == 1:

Verifica se o valor de n é igual a 0 ou 1.
Se for, retorna o valor atual de fat (que é 1).
O fatorial de 0 e 1 é igual a 1.
else:

Se nenhuma das condições anteriores for satisfeita, significa que n é maior que 1 e podemos calcular o fatorial recursivamente.
return n * fatorial_recursivo(n-1)

Aqui ocorre a chamada recursiva da função fatorial_recursivo com o valor n-1.
O resultado dessa chamada é multiplicado por n e retornado como resultado do fatorial.
print(fatorial_recursivo(5))

Chamada da função fatorial_recursivo passando o valor 5 como argumento.
O resultado do fatorial de 5 será impresso na tela.
Em resumo, o código define uma função recursiva chamada fatorial_recursivo que calcula o fatorial de um número inteiro
 não negativo. A função verifica se o número é válido, se é igual a 0 ou 1, ou se é maior que 1 para realizar o cálculo 
 recursivo. No final, o fatorial de 5 é calculado e impresso na tela. O resultado será 120, que é o fatorial de 5.
'''''
